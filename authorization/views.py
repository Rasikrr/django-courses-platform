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


# Create your views here.
class SignUp(CreateView):
    template_name = "authorization/register.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context["title"] = "Registration"
        return context


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


class LogOut(LogoutView):
    next_page = "index"