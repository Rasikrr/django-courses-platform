from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),
    path("confirmation/<str:email>/<uuid:code>/", Confirmation.as_view(), name="confirmation"),
    path("logout/", LogOut.as_view(), name="logout"),
]