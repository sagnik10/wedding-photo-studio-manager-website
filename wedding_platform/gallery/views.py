from django.shortcuts import render, get_object_or_404
from .models import Photo, Gallery


def gallery_list(request):
    photos = Photo.objects.all().order_by("-created")

    return render(
        request,
        "gallery/gallery_list.html",
        {
            "photos": photos,
        },
    )


def gallery_detail(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)

    photos = gallery.photos.all().order_by("-created")

    return render(
        request,
        "gallery/gallery_detail.html",
        {
            "gallery": gallery,
            "photos": photos,
        },
    )