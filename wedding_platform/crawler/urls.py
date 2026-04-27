from django.urls import path
from .views import run_crawler

app_name = "crawler"

urlpatterns = [
    path("run/", run_crawler, name="run"),
]