import base64
from django import forms
from django.contrib.auth import login, authenticate, get_user
from core.models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.core.exceptions import ValidationError
# from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os


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
        password = self.cleaned_data.get("password")
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


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}), label="Email")
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        html_email_template_path = "new-email.html"
        subject = "Password reset on Courses"
        text_content = ''
        # Making reset link
        context["link"] = f"/reset/{context['uid']}/{context['token']}"
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [self.cleaned_data["email"]])
        logo_path = os.path.join(settings.BASE_DIR, "authorization", "email_templates", "images", "logo-removebg-preview.png")
        with open(logo_path, "rb") as image:
            image_data = base64.b64encode(image.read()).decode("utf-8")
        context["logo"] = image_data

        html_content = get_template(html_email_template_path).render(context)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError("User with this email does not exist")
        return email

class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["old_password"]
        self.fields["new_password1"] = forms.CharField(widget=forms.PasswordInput(), label="New password")
        self.fields["new_password2"] = forms.CharField(widget=forms.PasswordInput(), label="Confirm password")

    def clean_new_password1(self):
        password_1 = self.cleaned_data["new_password1"]
        if len(password_1) < 8:
            raise forms.ValidationError("Password must has atleast 8 symbols")
        return password_1

    def clean_new_password2(self):
        password_2 = self.cleaned_data.get("new_password2")
        password_1 = self.cleaned_data.get("new_password1")
        if password_1 != password_2:
            raise forms.ValidationError("Passwords do not match")
        return password_2
