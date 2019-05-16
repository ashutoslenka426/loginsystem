from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']