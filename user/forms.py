from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), max_length=30, required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}), max_length=30, required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}), max_length=30, required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), max_length=30, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = UserModel
        fields = ("email", "first_name", "last_name", "address", "country", "password1", "password2")
    

class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = UserModel
        fields = ("username", "password",)
