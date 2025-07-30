from django.contrib import admin
from .models import Order, Products

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'price','amount_sold', 'created_at','updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
    ordering = ('-price',)
    readonly_fields = ('created_at', 'updated_at','amount_sold')  


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','user_id' ,'product','product_id', 'quantity', 'total_price', 'ordered_at')
    search_fields = (
        'user__id',            # search by user ID
        'user__first_name', 
        'user__last_name', 
        'product__id',         # search by product ID
        'product__title', 
    )
    list_filter = ('ordered_at',)
    ordering = ('-ordered_at',)
    readonly_fields = ('total_price',)
