import Users.models
from django.contrib import admin

from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', )
    ordering = ('email',)