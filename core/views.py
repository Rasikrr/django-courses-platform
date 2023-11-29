from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpRequest
from .forms import ContactForm, PersonalInfForm
from .models import ContactMessage, CustomUser, ProfileModel
from mixins import TitleMixin, MenuMixin


# Create your views here.
class Index(TitleMixin, TemplateView):
    template_name = "index.html"
    title = "Main page | Courses"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        print(self.request.user)
        return context


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
        return JsonResponse({'message': 'Our support will contact you shortly!'}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'message': 'Something went wrong, please try later'})


class Profile(TitleMixin, TemplateView):
    title = "Profile | Courses"
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        username = self.kwargs.get("username")
        user = CustomUser.objects.get(username=username)
        context["user"] = user
        profile = ProfileModel.objects.get(user=user)
        context["profile"] = profile
        return context


class PersonalInfEdit(SuccessMessageMixin, MenuMixin, TitleMixin, UpdateView):
    title = "Personal Information | Courses"
    template_name = "profile_edit/personal-inf.html"
    menu_section = "personal-inf"
    form_class = PersonalInfForm
    model = CustomUser
    success_message = "Your personal information was updated!"

    def get_object(self, queryset=None):
        return CustomUser.objects.get(username=self.kwargs.get("username"))

    def get_success_url(self):
        return self.request.path


class PaymentInfEdit(MenuMixin, TitleMixin, TemplateView):
    title = "Payment Information | Courses"
    template_name = "profile_edit/payments-inf.html"
    menu_section = "payments-inf"


class ProfileEdit(MenuMixin, TitleMixin, TemplateView):
    title = "Profile Edit | Courses"
    template_name = "profile_edit/profile-edit.html"
    menu_section = "profile-edit"


