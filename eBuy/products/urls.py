
from django.urls import path
from . import views

urlpatterns = [
  path('', views.productsView, name='home'),
  path('product/<int:id>/', views.product_detail, name='product_detail'),
  path('product/<str:category>/', views.product_by_category, name='products_by_category'),
  path('place_order/', views.place_order, name='place_order'),
]