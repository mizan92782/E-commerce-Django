from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Order, Products
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect


# Create your views here.
def productsView(request):
  
  products = Products.objects.all()
  context= {
      'products': products,
  }
  return render(request, 'products/home.html',context)


def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/detail.html', {'product': product})
  
def product_by_category(request, category):
    products = Products.objects.filter(category=category)
    return render(request, 'products/home.html', {
        'products': products,
        'selected_category': category
    })
    


# ! <----------------- orders view ----------------->

@login_required
def place_order(request):
    if request.method == "POST":
        product_id = request.POST.get("product")
        product = get_object_or_404(Products, id=product_id)

        Order.objects.create(
            user=request.user,            
            product=product,
            quantity=1  # or allow custom quantity
        )
        return redirect('home')
