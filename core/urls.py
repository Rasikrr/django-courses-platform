from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("about/", About.as_view(), name="about"),
    path("contact/", Contact.as_view(), name="contact"),
    path("profile/<str:username>", Profile.as_view(), name="profile"),
    path("profile/edit/pesonal-inf/<str:username>", PersonalInfEdit.as_view(), name="personal-inf"),
    path("profile/edit/payment/<str:username>", PaymentInfEdit.as_view(), name="payment-inf"),
    path("profile/edit/profile-edit/<str:username>", ProfileEdit.as_view(), name="profile-edit")
]