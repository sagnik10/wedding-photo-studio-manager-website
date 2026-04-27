from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wedding_platform.core.models import Order, Cart

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        next_url = request.GET.get("next")

        if not username or not password:
            messages.error(request, "Please fill in all fields.")
            return redirect("accounts:login")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(next_url if next_url else "core:home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("accounts:login")

    return render(request, "accounts/login.html")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("accounts:signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("accounts:signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("accounts:signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("core:home")

    return render(request, "accounts/signup.html")


@login_required
def dashboard_view(request):
    user = request.user

    orders = Order.objects.filter(user=user).order_by("-created_at")

    cart, _ = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.select_related("product")

    return render(request, "accounts/dashboard.html", {
        "orders": orders,
        "cart_items": cart_items,
        "user": user
    })


def logout_view(request):
    logout(request)
    return redirect("core:home")