from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment


@login_required
def payments_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")

        payment = Payment.objects.create(
            user=request.user,
            amount=amount,
        )

        return redirect("payments:success")

    return render(request, "payments/payment_form.html")


@login_required
def payment_success(request):
    return render(request, "payments/success.html")