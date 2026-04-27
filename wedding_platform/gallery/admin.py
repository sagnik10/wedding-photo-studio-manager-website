from django.contrib import admin
from .models import Gallery, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "is_private", "created")
    list_filter = ("is_private", "created")
    search_fields = ("title",)

    prepopulated_fields = {"slug": ("title",)}

    inlines = [PhotoInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "gallery", "created")
    search_fields = ("gallery__title",)