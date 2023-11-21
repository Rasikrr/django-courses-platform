from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),
    path("logout/", LogOut.as_view(), name="logout"),
]