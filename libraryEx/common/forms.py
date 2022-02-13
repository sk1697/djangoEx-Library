from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    #korname = forms.CharField(max_length=30)

    class Meta:
        model = get_user_model()
        #model = CustomUser
        fields = ("username","password1", "password2","korname", "email")