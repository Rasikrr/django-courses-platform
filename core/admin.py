from django.contrib import admin
from .models import CustomUser, ContactMessage, ProfileModel

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", )
    list_display_links = list_display


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "email", "created")
    list_display_links = ("user", "name", "email")
    

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "github", "phone", "address")
    list_display_links = list_display
