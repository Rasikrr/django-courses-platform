import uuid
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView, \
PasswordResetCompleteView, PasswordResetDoneView
from django.views import View
from datetime import timedelta
from django.utils.timezone import now
from .models import EmailVerification
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from core.models import ProfileModel
from .forms import SignUpForm, SignInForm, ResetPasswordForm, ChangePasswordForm
# Custom Mixin
from mixins import TitleMixin


# Create your views here.
class SignUp(SuccessMessageMixin, TitleMixin, CreateView):
    template_name = "authorization/register.html"
    form_class = SignUpForm
    title = "Registration | Courses"
    success_url = reverse_lazy("index")
    success_message = "You have successfuly created your account!\n" \
                      "Check your email to confirm it"

    def form_valid(self, form):
        response = super(SignUp, self).form_valid(form)
        user = form.save()
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")
        # Email Verification
        self.verification_email_sending(user=user)
        # Creating Profile
        form.create_profile()
        return response

    # Custom method
    def verification_email_sending(self, user):
        expiration = now() + timedelta(hours=48)
        email_verif = EmailVerification.objects.create(user=user, expiration=expiration, code=uuid.uuid4())
        email_verif.send_verification_email()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return super().get(request, *args, **kwargs)


class SignIn(TitleMixin, LoginView):
    template_name = "authorization/login.html"
    redirect_authenticated_user = "index"
    form_class = SignInForm
    title = "Login | Courses"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super(SignIn, self).form_valid(form)
        user = form.get_user()
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")
        return response


class Confirmation(TitleMixin, TemplateView):
    template_name = "authorization/confirmation.html"
    title = "Account Confirmation | Courses"
    has_time = True

    def get(self, request, *args, **kwargs):
        user = request.user
        email_verification_obj = EmailVerification.objects.filter(user=user)
        if email_verification_obj.exists():
            email_verification_obj = EmailVerification.objects.get(user=user)
            if email_verification_obj.expiration <= now():
                # Custom attribute
                self.has_time = False
            email_verification_obj.delete()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Confirmation, self).get_context_data(**kwargs)
        print("HAS TIME", self.has_time)
        if self.has_time:
            user = self.request.user
            if user.is_verified:
                context["confirmation"] = "You have already confirmed your account"
            else:
                user.is_verified = True
                user.save()
                context["confirmation"] = "Account confirmed successfully!"
        else:
            context["confirmation"] = "Your link has expired"
        context["has_time"] = self.has_time
        return context


class ResetPassword(TitleMixin, PasswordResetView):
    template_name = "authorization/reset_password.html"
    title = "Reser Password | Courses"
    form_class = ResetPasswordForm
    success_url = reverse_lazy("password_reset_done")


class PasswordChange(TitleMixin, PasswordResetConfirmView):
    title = "Change Password | Courses"
    form_class = ChangePasswordForm
    template_name = "authorization/password_reseting.html"
    success_url = reverse_lazy("password_reset_complete")

    def form_valid(self, form):
        response = super(PasswordChange, self).form_valid(form)
        print(self.request.user)
        return response


class PasswordResetDone(TitleMixin, PasswordResetDoneView):
    template_name = "authorization/password_reset_done.html"
    title = "Password reset | Courses"

class PasswordResetCompleted(TitleMixin, PasswordResetCompleteView):
    title = "Success | Courses"
    template_name = "authorization/reset_completed.html"



class LogOut(LogoutView):
    next_page = "index"