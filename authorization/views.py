import uuid
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from datetime import timedelta
from django.utils.timezone import now
from .models import EmailVerification
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm, SignInForm
# Cutom Mixin
from mixins import CommonMixin


# Create your views here.
class SignUp(CommonMixin, CreateView):
    template_name = "authorization/register.html"
    form_class = SignUpForm
    title = "Registration"

    def form_valid(self, form):
        response = super(SignUp, self).form_valid(form)
        user = form.save()
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")
        # Email Verification
        self.verification_email_sending(user=user)
        return response

    def get_success_url(self):
        return reverse_lazy("index")

    # Custom method
    def verification_email_sending(self, user):
        expiraion = now() + timedelta(hours=48)
        email_verif = EmailVerification.objects.create(user=user, expiration=expiraion, code=uuid.uuid4())
        email_verif.send_verification_email()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return super().get(request, *args, **kwargs)


class SignIn(LoginView):
    template_name = "authorization/login.html"
    redirect_authenticated_user = "index"
    form_class = SignInForm

    def get_success_url(self):
        return reverse_lazy("index")

    def form_valid(self, form):
        response = super(SignIn, self).form_valid(form)
        user = form.get_user()
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")
        return response


class Confirmation(CommonMixin, TemplateView):
    template_name = "authorization/confirmation.html"
    title = "Account Confirmation"

    def get(self, request, *args, **kwargs):
        user = request.user
        email_verification_obj = EmailVerification.objects.filter(user=user)
        if email_verification_obj.exists():
            user.is_verified = True
            email_verification_obj.delete()
            user.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Confirmation, self).get_context_data(**kwargs)
        if self.request.user.is_verified:
            context["confirmation"] = "You have already confirmed your account"
        else:
            context["confirmation"] = "Account confirmed successfuly!"
        return context


class LogOut(LogoutView):
    next_page = "index"