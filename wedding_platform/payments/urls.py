from django.urls import path
from .views import payments_view, payment_success

app_name = "payments"

urlpatterns = [
    path("", payments_view, name="pay"),
    path("success/", payment_success, name="success"),
]