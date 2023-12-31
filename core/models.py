from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def set_default_username(self):
        self.username = f"{self.first_name}_{self.last_name}_{self.id}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.username})


class ContactMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=256, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.name}, email: {self.email}"


class ProfileModel(models.Model):
    SPECIALIZATION_CHOICES = (
        ("backend", "Backend Developer"),
        ("frontend", "Frontend Developer"),
        ("fullstack", "Full Stack Developer"),
        ("android", "Mobile Android Developer"),
        ("ios", "Mobile IOS Developer"),
        ("gamedev", "Game Developer")
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_images", default="img-profile-default.png")
    website = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.CharField(null=True, blank=True, max_length=100)
    instagram = models.CharField(null=True, blank=True, max_length=100)
    facebook = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, default=None, blank=True, null=True)

    def __str__(self):
        return f"Profile of user: {self.user}"