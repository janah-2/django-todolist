from django import forms
from django.forms import ModelForm
from .models import *

class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=200, widget= forms.TextInput(attrs={'placeholder':'Add new list...'}))
    check = forms.BooleanField(required=False)