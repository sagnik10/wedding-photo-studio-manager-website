from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from urllib.parse import quote
from wedding_platform.booking.models import Bookings


@login_required
def booking_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        event_date = request.POST.get("event_date")
        package = request.POST.get("package")
        message = request.POST.get("message")

        if not name or not email or not event_date:
            return redirect("booking:booking")

        Booking.objects.create(
            user=request.user,
            name=name,
            email=email,
            package=package,
            event_date=event_date,
            message=message,
            status="pending"
        )

        msg = quote(
            f"Hi, I just made a booking.\n\n"
            f"Name: {name}\n"
            f"Package: {package}\n"
            f"Date: {event_date}"
        )

        return redirect(f"/booking/success/?msg={msg}")

    return render(request, "booking/booking.html")


@login_required
def booking_success(request):
    msg = request.GET.get("msg", "")
    whatsapp_link = f"https://wa.me/447428664274?text={msg}"

    return render(request, "booking/success.html", {
        "whatsapp_link": whatsapp_link
    })