import re

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from inventoryapp.user.customexceptions.custom_exceptions import *


class SignUpForm(forms.Form):

    name = forms.CharField(label='Name ', widget=forms.TextInput(attrs={'style': 'width: 100%'}), max_length=100)
    email = forms.CharField(label='Email ', widget=forms.TextInput(attrs={'style': 'width: 100%'}), max_length=100)
    password = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'style': 'width: 100%'}),
                               max_length=100)
    address = forms.CharField(label='Address ', widget=forms.Textarea(attrs={'style': 'width: 100%'}), max_length=240)

    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

    class EmailAlreadyExists(EmailAlreadyExists):
        pass

    class MustContainSpecialCharacter(MustContainSpecialCharacter):
        pass

    class PasswordTooShort(PasswordTooShort):
        pass

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            self.check_if_exists(email=email)
        except self.EmailAlreadyExists as ex:
            raise ValidationError(ex.message)

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        try:
            self.check_password(password=password)
        except (self.PasswordTooShort, self.MustContainSpecialCharacter) as ex:
            raise ValidationError(ex.message)
        return password

    def check_if_exists(self, email):
        if get_user_model().objects.filter(email=email).exists():
            raise self.EmailAlreadyExists

    def check_password(self, password):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise self.PasswordTooShort
        elif not re.search(r'[\W]+', password):
            raise self.MustContainSpecialCharacter
