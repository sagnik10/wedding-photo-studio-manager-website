from django.contrib import admin
from .models import SEO
from .city_models import CityPage


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = ("page_slug", "title")
    search_fields = ("page_slug", "title")


@admin.register(CityPage)
class CityPageAdmin(admin.ModelAdmin):
    list_display = ("city", "slug")
    search_fields = ("city",)