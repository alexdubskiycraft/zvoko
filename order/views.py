from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Product, Basket
from django.http import JsonResponse

@login_required
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('guantity', 1))
    product = Product.objects.get(id=product_id)

    basket_product, created = Basket.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': quantity}
    )  

    if not created:
        basket_product.quantity += quantity
        basket_product.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))      

def total_products_in_cart(request):
    if not request.user.is_authenticated:
        return JsonResponse({'total': 0})

    basket_products = Basket.objects.filter(user=request.user)
    total = sum(item.quantity for item in basket_products)

    return JsonResponse({'total': total})      