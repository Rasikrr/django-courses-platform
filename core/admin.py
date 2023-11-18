from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", )
    list_display_links = list_display

admin.site.register(CustomUser, CustomUserAdmin )