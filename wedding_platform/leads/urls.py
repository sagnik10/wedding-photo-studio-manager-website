from django.urls import path
from .views import leads_view

app_name = "leads"

urlpatterns = [
    path("", leads_view, name="leads"),
]