import base64
import os
from django.db import models
from core.models import CustomUser
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


# Create your models here.
class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"Email verification object to {self.user.email}"

    # Custom method
    def send_verification_email(self):
        html_email_template_path = "account-confirmation.html"
        subject = f"Account confirmation for {self.user.username}"
        text_content = ""
        link = settings.DOMAIN_NAME + reverse("confirmation", kwargs={"email": self.user.email,
                                           "code": self.code
                                           })
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [self.user.email])
        logo_path = os.path.join(settings.BASE_DIR, "authorization", "email_templates", "images",
                                 "logo-removebg-preview.png")
        with open(logo_path, "rb") as image:
            image_data = base64.b64encode(image.read()).decode("utf-8")
        context = {}
        context["logo"] = image_data
        context["link"] = link
        html_content = get_template("account-confirmation.html").render(context)
        msg.attach_alternative(html_content, "text/html")
        msg.send()