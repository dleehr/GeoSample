# Create your views here.
from django.contrib.gis.geos.point import Point

from django.shortcuts import render
from world.forms import SearchForm
from world.models import WorldBorder


def search_form(request):
	if request.method == 'POST':
		# Do a search
		form = SearchForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			# Now find the objects
			feature = WorldBorder.objects.get(mpoly__intersects=cd['point'])
			response_dict = {'feature': feature}
			return render(request, 'search_results.html', response_dict)

	else:
		form = SearchForm
		# gis/openlayers-osm.html?
		return render(request, 'search_form.html', {'form': form })