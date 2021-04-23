from django.forms import ModelForm
from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "phone_number",
            "website",
            "city",
            "country",
            "zip_code",
        ]
