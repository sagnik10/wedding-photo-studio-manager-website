from django.db import models
from django.conf import settings


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=200)
    email = models.EmailField()

    event_date = models.DateField()

    message = models.TextField(blank=True)

    total_price = models.FloatField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.event_date} | {self.status}"


class BookingItem(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        "core.Product",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    package_name = models.CharField(max_length=255, blank=True)

    quantity = models.PositiveIntegerField(default=1)

    price = models.FloatField()

    def get_name(self):
        if self.product:
            return self.product.name
        return self.package_name

    def total_price(self):
        return self.quantity * self.price