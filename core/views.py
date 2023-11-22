from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.views import View
from .forms import ContactForm
from mixins import CommonMixin


# Create your views here.
class Index(CommonMixin, TemplateView):
    template_name = "index.html"
    title = "Main page | Courses"


class About(CommonMixin, TemplateView):
    template_name = "about.html"
    title = "About"


class Contact(CommonMixin, CreateView):
    template_name = "contact.html"
    title = "Contacts"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        response = super(Contact, self).form_valid(form)
        user = self.request.user
        contact_message = form.save(commit=False)
        contact_message.user = user
        contact_message.save()
        return response





