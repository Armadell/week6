
from dataclasses import field
from socket import fromshare
from django import forms
from .models import book
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm#it is a
#build in module inherits form modelform
 
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()


    class Meta:
        model=User
        fields=['username','email','password1','password2']
class  BookCreate(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'


