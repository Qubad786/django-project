from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}), max_length=100)
