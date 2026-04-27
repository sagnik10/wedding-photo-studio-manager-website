from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead


def leads_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if not name or not email:
            messages.error(request, "Name and Email are required.")
            return redirect("leads:leads")

        lead = Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        score = 0
        if message:
            score += 5
        if phone:
            score += 5

        lead.score = score
        lead.save()

        messages.success(request, "Your inquiry has been submitted.")
        return redirect("core:home")

    return render(request, "leads/contact.html")