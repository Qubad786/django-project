from django import forms
from django.core.exceptions import ValidationError


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%', 'readonly': 'readonly'}),
                                   max_length=255)
    kind = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%', 'readonly': 'readonly'}),
                           max_length=255)
    brand = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%', 'readonly': 'readonly'}),
                            max_length=255)
    units = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%', 'readonly': 'readonly'}))

    def clean_units(self):
        try:
            units = int(self.cleaned_data.get('units'))
            return units
        except:
            raise ValidationError('units must be in numbers only.')
