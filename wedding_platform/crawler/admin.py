from django.contrib import admin
from .models import CrawlTarget, CrawlResult


@admin.register(CrawlTarget)
class CrawlTargetAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "url")
    search_fields = ("name", "region")


@admin.register(CrawlResult)
class CrawlResultAdmin(admin.ModelAdmin):
    list_display = ("target", "created_at")