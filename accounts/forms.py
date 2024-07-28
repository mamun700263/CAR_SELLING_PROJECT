from typing import Any
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    """This form will ask to give first_name, last_name , username,email and they are all must needed"""
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'first_name' : forms.TextInput(attrs={'required': True}),
            'last_name' : forms.TextInput(attrs={'required': True}),
            'email' : forms.TextInput(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True




class InformationChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

