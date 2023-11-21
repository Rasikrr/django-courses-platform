from django.db import models
from core.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"Email verification object to {self.user.email}"

    def send_verification_email(self):
        send_mail(
            "Subject",
            "Message",
            settings.EMAIL_HOST_USER,
            (self.user.email,)
        )
