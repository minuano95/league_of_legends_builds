from django.utils.translation import gettext as _
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30,
                                 label='First Name',
                                 widget=forms.TextInput(
                                     attrs={"type": "text",
                                    "placeholder": _("First Name")
                                            }
                                    )
                                 )
    last_name = forms.CharField(max_length=30,
                                 label='Last Name',
                                 widget=forms.TextInput(
                                     attrs={"type": "text",
                                        "placeholder": _("Last Name")
                                        }
                                    )
                                )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.id = self.cleaned_data["id"]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
