from django.urls import path
from .views import seo_view

app_name = "seo"

urlpatterns = [
    path("", seo_view, name="dashboard"),
]