from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = order 
        fields = '__all__'
        exclude =['date_modified', 'm_user']

class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        exclude =['date_modified', 'm_user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
