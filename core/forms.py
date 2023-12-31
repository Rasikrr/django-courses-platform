from django import forms
from .models import ContactMessage, ProfileModel, CustomUser


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "message", "subject")
        widgets = {
            "message": forms.Textarea(attrs={"class": "form-control w-100",
                                             "placeholder": "Enter Message",
                                             "cols": "30",
                                             "rows": "9",
                                             "onfocus": "this.placeholder = ''",
                                             "onblur": "this.placeholder = 'Enter Message'"
                                             }),

            "name": forms.TextInput(attrs={"class": "form-control valid",
                                           "type": "text",
                                           "placeholder": "Enter your name",
                                           "onfocus": "this.placeholder = ''",
                                           "onblur": "this.placeholder = 'Enter your name'"
                                           }),

            "email": forms.TextInput(attrs={"class": "form-control valid",
                                            "type": "email",
                                            "onfocus": "this.placeholder = ''",
                                            "onblur": "this.placeholder = 'Enter your email'",
                                            "placeholder": "Email"
                                            }),

            "subject": forms.TextInput(attrs={"class": "form-control",
                                              "type": "text",
                                              "onfocus": "this.placeholder = ''",
                                              "onblur": "this.placeholder = 'Enter your subject'",
                                              "placeholder": "Enter Subject"
                                              })
        }

    def save(self, commit=True):
        contact_message = super().save(commit=False)
        return contact_message


class PersonalInfForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username")
        widgets = {
            "first_name": forms.TextInput(attrs={"type": "text",
                                                 "name": "firstName"}),
            "last_name": forms.TextInput(attrs={"type": "text",
                                                "name": "surName"}),
            "username": forms.TextInput(attrs={"type": "text",
                                               "name": "username"})
        }

