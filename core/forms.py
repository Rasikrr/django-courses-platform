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


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Firstname", widget=forms.TextInput(attrs={"class": "col-sm-9 text-secondary inputs-2",
                                                                                  "name": "first_name",
                                                                                  "type": "text",
                                                                                  "placeholder": "Your name"
                                                                                  }))

    last_name = forms.CharField(label="Lastname", widget=forms.TextInput(attrs={"class": "col-sm-9 text-secondary inputs-2",
                                                                                "name": "last_name",
                                                                                "type": "text",
                                                                                "placeholder": "Your lastname"
                                                                                }))

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "col-sm-9 text-secondary inputs-2",
                                                                               "name": "fullname",
                                                                               "type": "text",
                                                                               "placeholder": "Your username"
                                                                               }))

    class Meta:
        model = ProfileModel
        fields = ("website", "github", "twitter", "instagram", "facebook", "phone", "address")
        widgets = {
            "website": forms.URLInput(attrs={"class": "text-secondary inputs",
                                             "placeholder": "Your Website",
                                             "name": "email",
                                             "type": "url"}),

            "github": forms.URLInput(attrs={"class": "text-secondary inputs",
                                            "placeholder": "Your Github",
                                            "name": "github",
                                            "type": "url"}),

            "twitter": forms.URLInput(attrs={"class": "text-secondary inputs",
                                             "placeholder": "Your Twitter",
                                             "name": "twitter",
                                             "type": "url"}),

            "instagram": forms.URLInput(attrs={"class": "text-secondary inputs",
                                               "placeholder": "Your Instagram",
                                               "name": "instagram",
                                               "type": "url"}),

            "facebook": forms.URLInput(attrs={"class": "text-secondary inputs",
                                              "placeholder": "Your Facebook",
                                              "name": "facebook",
                                              "type": "url"}),

            "phone": forms.NumberInput(attrs={"class": "col-sm-9 text-secondary inputs-2",
                                              "placeholder": "Your phone",
                                              "name": "address",
                                              "type": "number"}),

            "address": forms.TextInput(attrs={"class": "col-sm-9 text-secondary inputs-2",
                                              "placeholder": "Your address",
                                              "name": "address",
                                              "type": "text"
                                              })
        }


