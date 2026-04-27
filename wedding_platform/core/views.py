from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.http import JsonResponse
import json

from .models import Product, Cart, CartItem, Order, OrderItem, Lead
from wedding_platform.booking.models import Booking, BookingItem


def get_photos():
    folder = Path(settings.MEDIA_ROOT) / "gallery" / "photos"
    images = []

    if folder.exists():
        for file in sorted(folder.iterdir()):
            if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                if "logo" not in file.name.lower():
                    images.append(f"gallery/photos/{file.name}")

    return images[:20]


def get_store_photos():
    folder = Path(settings.MEDIA_ROOT) / "gallery" / "photos"
    images = []

    if folder.exists():
        for file in sorted(folder.iterdir()):
            if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                if "logo" not in file.name.lower():
                    images.append(file.name)

    return images


def home(request):
    photos = get_photos()
    hero = Product.objects.filter(name="Hero Cover").order_by('-id').first()

    return render(request, "core/home.html", {
        "photos": photos,
        "hero": hero
    })


def about(request):
    return render(request, "core/about.html", {"photos": get_photos()})


def portfolio(request):
    return render(request, "core/portfolio.html", {"photos": get_photos()})


def packages(request):
    return render(request, "core/packages.html")


@login_required
def booking(request, package):
    data = {
        "premium-wedding": {"title": "Premium Wedding Photography Package", "price": 399.00},
        "premium-plus": {"title": "Premium Plus Wedding Photography Package", "price": 599.00},
        "premium-vip": {"title": "Premium VIP Wedding Photography Package", "price": 699.00},
        "wedding-cinematography": {"title": "Wedding Cinematography", "price": 699.00},
        "international-weddings": {"title": "International Weddings", "price": 950.00},
        "model-photoshoot": {"title": "Professional Model Photoshoot", "price": 250.00},
        "family-portraits": {"title": "Professional Family Portraits", "price": 375.00},
        "corporate-headshots": {"title": "Corporate Headshots | Group and Solo", "price": 375.00},
        "mother-daughter": {"title": "Mother and Daughter Photoshoot", "price": 199.00},
        "father-son": {"title": "Father & Son Photoshoot", "price": 199.00},
        "corporate-photography": {"title": "Corporate Photographes", "price": 275.00},
        "corporate-adverts": {"title": "Corporate Adverts", "price": 575.00},
        "pet-photoshoot": {"title": "Pet Photoshoot in Professional Studio", "price": 199.00},
    }

    package_data = data.get(package, data["premium-plus"])

    if request.method == "POST":
        product, _ = Product.objects.get_or_create(
            name=package_data["title"],
            defaults={"price": package_data["price"]}
        )

        cart, _ = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            item.quantity += 1
        else:
            item.quantity = 1

        item.save()

        return redirect("core:cart")

    return render(request, "core/booking.html", {"pkg": package_data})


def contact(request):
    return render(request, "core/contact.html")


def store(request):
    products = Product.objects.exclude(image='')

    category = request.GET.get("category")
    sort = request.GET.get("sort")

    if category:
        products = products.filter(name__icontains=category)

    if sort == "low":
        products = products.order_by("price")
    elif sort == "high":
        products = products.order_by("-price")

    return render(request, "core/store.html", {
        "products": products,
        "selected_category": category,
        "selected_sort": sort,
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    qty = int(request.GET.get("qty", 1))

    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += qty
    else:
        item.quantity = qty

    item.save()

    return redirect("core:cart")


@login_required
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    qty = int(request.GET.get("qty", 1))

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()

    CartItem.objects.create(cart=cart, product=product, quantity=qty)

    return redirect("core:checkout")


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product")
    total = sum(item.total_price() for item in items)

    return render(request, "core/cart.html", {
        "items": items,
        "total": total
    })


@login_required
@require_POST
def update_cart(request):
    cart = Cart.objects.get(user=request.user)

    for item in cart.items.all():
        qty = request.POST.get(f"quantity_{item.id}")
        if qty:
            item.quantity = int(qty)
            item.save()

    return redirect("core:cart")


@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect("core:cart")


@login_required
def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product")

    total = sum(item.total_price() for item in items)

    if request.method == "POST":

        if not items.exists():
            return redirect("core:cart")

        order = Order.objects.create(
            user=request.user,
            total=total,
            status="pending"
        )

        booking = Booking.objects.create(
            user=request.user,
            name=request.user.username,
            email=request.user.email,
            event_date=timezone.now().date(),
            message="Booked via checkout",
            total_price=total,
            status="pending"
        )

        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            BookingItem.objects.create(
                booking=booking,
                product=item.product,
                package_name=item.product.name,
                quantity=item.quantity,
                price=item.product.price
            )

        cart.items.all().delete()

        return redirect("core:order_success")

    return render(request, "core/checkout.html", {
        "items": items,
        "total": total
    })


@login_required
def order_success(request):
    order = Order.objects.filter(user=request.user).order_by("-created_at").first()

    if not order:
        return redirect("core:store")

    items = order.items.select_related("product")

    message = "Hi, I just placed an order:\n"

    for item in items:
        message += f"{item.product.name} x {item.quantity}\n"

    message += f"\nTotal: £{order.total}"

    import urllib.parse
    whatsapp_message = urllib.parse.quote(message)

    whatsapp_link = f"https://wa.me/447428664274?text={whatsapp_message}"

    return render(request, "core/order_success.html", {
        "order": order,
        "items": items,
        "whatsapp_link": whatsapp_link
    })


@login_required
def services_cart(request):
    return render(request, "core/services_cart.html", {
        "items": [],
        "total": 0
    })


def chatbot_lead(request):
    if request.method == "POST":
        data = json.loads(request.body)

        lead = Lead.objects.create(
            name=data.get("name"),
            phone=data.get("phone"),
            event_date=data.get("date"),
            location=data.get("location") or "N/A",
            budget=data.get("budget") or "N/A",
            hours=data.get("hours") or "N/A",
            videography=data.get("video") or "No",
            guests=data.get("guests") or "N/A",
            style=data.get("style") or "N/A",
            user=request.user if request.user.is_authenticated else None
        )

        return JsonResponse({"status": "success", "id": lead.id})