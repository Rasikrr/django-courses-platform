from django.db import models
from core.models import CustomUser
from django.urls import reverse, reverse_lazy
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
        subject = f"Account confirmation for {self.user.username}"
        link = settings.DOMAIN_NAME + reverse("confirmation", kwargs={"email": self.user.email,
                                               "code": self.code
                                               })
        message = f"To confirm your account, please follow this link {link}"
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(self.user.email,)
        )
