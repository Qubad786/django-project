from django import forms


class SignInForm(forms.Form):
    email = forms.CharField( widget=forms.TextInput(attrs={'style': 'width: 100%'}), max_length=100)
    password = forms.CharField( widget=forms.PasswordInput(attrs={'style': 'width: 100%'}), max_length=100)
    remember_me = forms.BooleanField(required=False)