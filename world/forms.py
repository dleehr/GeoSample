from django import forms

class SearchForm(forms.Form):
	lat = forms.CharField('Latitude')
	lon = forms.CharField('Longitude')