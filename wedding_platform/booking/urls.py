from django.urls import path
from .views import booking_view, booking_success

app_name = "booking"

urlpatterns = [
    path("", booking_view, name="booking"),
    path("success/", booking_success, name="success"),
]