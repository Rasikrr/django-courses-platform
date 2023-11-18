from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.generic import ListView, CreateView, DetailView, FormView
from .forms import SignUpForm


# Create your views here.
def index(request):
    print(request.user.first_name)
    return render(request, "index.html")

def signin(request):
    return render(request, "login.html")

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registration"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()  # This already saves the user
        login(self.request, user, backend="Django_courses_website.backends.EmailBackend")  # Log in the user
        return response


def about(request):
    return render(request, "index.html")
