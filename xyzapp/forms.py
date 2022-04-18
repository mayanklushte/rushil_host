from socket import fromshare
from django import forms
from xyzapp.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields="__all__" 