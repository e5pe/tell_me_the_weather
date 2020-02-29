from django.forms import Form, TextInput, CharField


class SearchForm(Form):
    search = CharField(label='',
                       widget=TextInput(attrs={'class': 'input',
                                               'placeholder': 'City Name'})
                       )

    class Meta:
        fields = ('search')
