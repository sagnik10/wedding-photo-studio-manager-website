from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=75.00)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    package = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.package} - {self.date}"


class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    event_date = models.DateField()
    location = models.CharField(max_length=255, default="N/A")
    budget = models.CharField(max_length=50, default="N/A")
    hours = models.CharField(max_length=50, default="N/A")
    videography = models.CharField(max_length=10, default="No")
    guests = models.CharField(max_length=50, default="N/A")
    style = models.CharField(max_length=50, default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.event_date}"