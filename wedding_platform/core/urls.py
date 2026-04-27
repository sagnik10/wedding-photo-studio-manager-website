from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("packages/", views.packages, name="packages"),
    path("booking/<str:package>/", views.booking, name="booking"),
    path("contact/", views.contact, name="contact"),
    path("store/", views.store, name="store"),

    path("cart/", views.cart_view, name="cart"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("buy-now/<int:product_id>/", views.buy_now, name="buy_now"),
    path("services-cart/", views.services_cart, name="services_cart"),

    path("update-cart/", views.update_cart, name="update_cart"),
    path("remove-item/<int:item_id>/", views.remove_item, name="remove_item"),

    path("checkout/", views.checkout, name="checkout"),
    path("order-success/", views.order_success, name="order_success"),

    path("chatbot-lead/", views.chatbot_lead, name="chatbot_lead"),
]