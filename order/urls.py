from django.urls import path
from order import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("total-products-in-cart/", views.total_products_in_cart, name="total_products_in_cart")    
]