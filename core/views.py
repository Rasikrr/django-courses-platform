from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.views import View
from django.http import JsonResponse, HttpRequest
from .forms import ContactForm
from .models import ContactMessage
from mixins import TitleMixin


# Create your views here.
class Index(TitleMixin, TemplateView):
    template_name = "index.html"
    title = "Main page | Courses"


class About(TitleMixin, TemplateView):
    template_name = "about.html"
    title = "About"


class Contact(TitleMixin, CreateView):
    template_name = "contact.html"
    title = "Contacts"
    form_class = ContactForm
    model = ContactMessage

    def form_valid(self, form):
        user = self.request.user
        contact_message = form.save(commit=False)
        contact_message.user = user
        contact_message.save()
        return JsonResponse({'message': 'success'}, status=200)



