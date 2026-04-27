from django.urls import path
from .views import gallery_list, gallery_detail

app_name = "gallery"

urlpatterns = [
    path("", gallery_list, name="list"),
    path("<slug:slug>/", gallery_detail, name="detail"),
]