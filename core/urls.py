from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("signin", views.login, name="signin"),
    path("about", views.about, name="about"),
]