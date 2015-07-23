import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProfileForm(forms.Form):
    name = forms.CharField(label='Name ',
                           widget=forms.TextInput(attrs={'style': 'width: 100%', }),
                           max_length=100)
    email = forms.CharField(label='Email ',
                            widget=forms.TextInput(attrs={'style': 'width: 100%', 'readonly': 'readonly'}),
                            max_length=100)
    password = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'style': 'width: 100%'}),
                               max_length=100)
    address = forms.CharField(label='Address ', widget=forms.Textarea(attrs={'style': 'width: 100%'}), max_length=240)

    CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("Password is too short.")
        elif not re.search(r'[\W]+', password):
            raise ValidationError("Password must contain a special character.")
        return password
