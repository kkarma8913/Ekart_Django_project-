from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username','password1','password2']