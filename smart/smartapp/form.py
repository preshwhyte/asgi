from dataclasses import field
from socket import fromshare
from .models import member, Comment
from django.forms import ModelForm
from django import forms


class memberform(forms.ModelForm):
    class Meta:
        model=member
        fields=('Firstname', 'Lastname', 'other', 'email', 'address', 'phone')

class postform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name', 'post')

        