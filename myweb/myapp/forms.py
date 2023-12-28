# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ContactSubmission
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactSubmission
#         fields = ['name', 'email', 'message']
