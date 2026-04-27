from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "score", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("name", "email", "phone")
    ordering = ("-created",)