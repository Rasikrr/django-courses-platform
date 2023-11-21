from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
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
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")  # Log in the user
        return response


    def get_success_url(self):
        return reverse_lazy("index")



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