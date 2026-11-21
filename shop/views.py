from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from shop.models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required


class CategoryList(ListView):
    model = Category
    template_name = "shop/category_list.html"
    context_object_name = "categories"
    ordering = ["priority"]
    

class ProductList(ListView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        cat = self.kwargs.get("cat")
        products = Product.objects.all()

        if cat:
            return products.filter(category = cat)

        raise Http404("Категорію не знайдено")

class ProductDetail(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"
    slug_field = "id"
    slug_url_kwarg = "slug"       








