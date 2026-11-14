from django.urls import path
from shop import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.CategoryList.as_view(), name="category_list"),
    path("category/<int:cat>/", views.ProductList.as_view(), name="product_list"),
    path("product/<slug:slug>/", views.ProductDetail.as_view(), name="product_detail"),
]