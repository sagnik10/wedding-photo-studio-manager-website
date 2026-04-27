from django.shortcuts import render
from .models import SEO


def seo_view(request):
    data = SEO.objects.all()

    return render(
        request,
        "seo/dashboard.html",
        {"data": data},
    )