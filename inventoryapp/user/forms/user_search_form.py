from django import forms


class UserSearchForm(forms.Form):
    RESULTS_CHOICES = [('', 'All'), ('username', 'User name'), ('userprofile__gender', 'Gender'),
                       ('email', 'Email address'),
                       ('userprofile__address', 'Residence address')]

    email = forms.CharField(label='Email ', required=False, widget=forms.TextInput(attrs={'style': 'width: 100%'}),
                            max_length=100)
    start_date = forms.DateField(label='Start date ', required=False,
                                 widget=forms.DateInput(attrs={'style': 'width: 100%', 'type': 'date'}))
    end_date = forms.DateField(label='End Date ', required=False,
                               widget=forms.DateInput(attrs={'style': 'width: 100%', 'type': 'date'}))

    result_should_include = forms.ChoiceField(required=False, choices=RESULTS_CHOICES)


