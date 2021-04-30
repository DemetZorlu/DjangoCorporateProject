from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    menuid = forms.IntegerField(label='Searchsel')
