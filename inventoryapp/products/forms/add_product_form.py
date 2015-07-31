from decimal import Decimal
from django import forms
from django.core.exceptions import ValidationError


class AddProductForm(forms.Form):

    KIND_CHOICES = [('all-season', 'All Season'), ('all-terrain', 'All Terrain'),
                    ('mud', 'Mud'), ('snow', 'snow/winter'), ('low-profile', 'Low Profile'),
                    ('off-road', 'Off Road'), ('performance', 'Performance'), ('suv', 'SUV'),
                    ('truck', 'Truck'),]

    PRODUCT_CHOICES = [('tire', 'Tire'),]

    name = forms.ChoiceField(choices=PRODUCT_CHOICES)
    kind = forms.ChoiceField(choices=KIND_CHOICES)
    brand = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}), max_length=255)
    units = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    stock_price = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    profit_in_percentage = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))

    def clean_units(self):
        try:
            units = int(self.cleaned_data.get('units'))
            return units
        except:
            raise ValidationError('units must be in numbers only.')

    def clean_stock_price(self):
        try:
            stock_price = Decimal(self.cleaned_data.get('stock_price'))
            return stock_price
        except:
            raise ValidationError('stock price must be a decimal value.')

    def clean_profit_in_percentage(self):
        try:
            profit_in_percentage = Decimal(self.cleaned_data.get('profit_in_percentage'))
            return profit_in_percentage
        except:
            raise ValidationError('profit must be a decimal value.')


