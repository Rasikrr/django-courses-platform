from django import forms
from django.contrib.auth import login, authenticate, get_user
from core.models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import AuthenticationForm
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
        if len(password_2) < 8 or len(password_1) < 8:
            raise ValidationError("Password must has at least 8 symbols")
        return password_1

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data.get("password"))
        user.set_default_username()
        user.save()
        return user


class SignInForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}), label="Email")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["username"]
        self.fields["password"] = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}))

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise ValidationError("Password must have atleast 8 symbols")
        return password

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError("Invalid email or password")
            cleaned_data['user'] = user
        return cleaned_data

    def get_user(self):
        return self.cleaned_data["user"]