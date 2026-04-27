from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from wedding_platform.booking.models import Booking
from wedding_platform.core.models import Order
from .models import User


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    readonly_fields = ("event_date", "status", "total_price", "created")


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ("total", "status", "created_at")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = ("id", "username", "email", "phone", "is_staff", "is_active")
    search_fields = ("username", "email", "phone")

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("phone",),
        }),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("phone",),
        }),
    )

    inlines = [BookingInline, OrderInline]