from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetConfirmView


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),
    path("confirmation/<str:email>/<uuid:code>/", Confirmation.as_view(), name="confirmation"),
    path("logout/", LogOut.as_view(), name="logout"),
    path("password-reset/", ResetPassword.as_view(), name="password-reset"),

    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordChange.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleted.as_view(), name='password_reset_complete'),


]