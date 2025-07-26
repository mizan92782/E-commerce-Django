from django.shortcuts import get_object_or_404, render
from .models import Products

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