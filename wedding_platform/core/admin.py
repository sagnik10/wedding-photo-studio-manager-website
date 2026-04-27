from django.contrib import admin
from .models import Product, Cart, CartItem, Booking, Lead


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    search_fields = ("name",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "package", "date", "time")
    list_filter = ("package", "date")
    search_fields = ("user__username", "package")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "event_date", "budget", "style", "created_at")
    list_filter = ("event_date", "budget", "style")
    search_fields = ("name", "phone", "location")
    ordering = ("-created_at",)