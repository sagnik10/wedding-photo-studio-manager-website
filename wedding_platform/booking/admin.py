from django.contrib import admin
from .models import Booking, BookingItem


class BookingItemInline(admin.TabularInline):
    model = BookingItem
    extra = 0


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event_date", "total_price", "status", "created")
    inlines = [BookingItemInline]