from django import forms

class SearchForm(forms.Form):
    minPrice = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'minPrice_field'}))
    maxPrice = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'maxPrice_field'}))