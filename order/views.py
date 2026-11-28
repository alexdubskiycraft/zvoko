from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView
from .models import *
from django.http import JsonResponse
from django.urls import reverse_lazy

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

class BasketView(ListView):
    model = Basket
    template_name = "order/basket.html"
    context_object_name = "items"

    def get_queryset(self):
        items = Basket.objects.all()
        return items.filter(user=self.request.user)

#class OrderCreate(CreateView):
#    model = Order
#    form_class = OrderForm
#    template_name = "order/order_form.html"

#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super().form_valid(form)

#    def get_success_url(self):
#        return reverse_lazy("order_success", kwargs={"slug": self.object.id})