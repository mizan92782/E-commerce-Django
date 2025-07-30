import Users.models
from django.contrib import admin

from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_active','address', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', )
    ordering = ('email',)