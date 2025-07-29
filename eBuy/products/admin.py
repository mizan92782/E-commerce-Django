from django.contrib import admin
from .models import Products

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'price','amount_sold', 'created_at','updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
    ordering = ('-price',)
    readonly_fields = ('created_at', 'updated_at','amount_sold')  
    
