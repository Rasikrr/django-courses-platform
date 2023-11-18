from django import forms
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    password_2 = forms.CharField(label="Confirm password",
                                 widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}))

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
        }


    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password")
        password_2 = self.cleaned_data.get("password_2")
        if password_1 != password_2:
            raise ValidationError("Passwords are not the same")
        return password_1

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data.get("password"))
        user.save()
        return user


