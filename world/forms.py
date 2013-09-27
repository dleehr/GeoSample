from django.contrib.gis import forms

class SearchForm(forms.Form):
	point = forms.PointField(widget=forms.OpenLayersWidget())
