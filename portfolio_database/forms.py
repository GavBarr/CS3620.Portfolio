from django import forms
from .models import Contacts
from .models import Portfolio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['contact_name', 'contact_email', 'contact_message']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project_name', 'project_description', 'project_image']




