from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'is_employer', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            "placeholder": "Enter Username",
            "class": "form-control"
        }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            "placeholder": "Enter Email",
            "class": "form-control"
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Enter Password",
            "class": "form-control"
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Repeat Password",
            "class": "form-control"
     }))

