from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput

class UserForm(forms.ModelForm):
    signup = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']