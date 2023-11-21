from django.contrib import admin
from .models import EmailVerification
# Register your models here.


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "expiration")
    list_display_links = ("user",)
    readonly_fields = ("created",)

