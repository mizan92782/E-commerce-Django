from django.contrib import admin
from .models import Products  # Import the Products model

# Register your models here.

@admin.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','owner','title', 'price', 'count', 'category')  # Fields to display in the admin list view
    search_fields = ('owner', 'title')  # Fields to search in the admin interface
    list_filter = ('owner',) 
    readonly_fields=('owner',)
    
    
    def save_model(self, request, obj, form, change):
        if not change:  # only set on create, not update
            obj.owner = request.user
        super().save_model(request, obj, form, change)
