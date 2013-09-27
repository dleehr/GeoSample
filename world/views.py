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
			lat = float(cd['lat'])
			lon = float(cd['lon'])
			# Now find the objects
			p = Point(lat, lon)
			feature = WorldBorder.objects.get(mpoly__intersects=p)
			response_dict = {'lat': lat, 'lon': lon, 'feature': feature}
			return render(request, 'search_results.html', response_dict)

	else:
		form = SearchForm
		return render(request, 'search_form.html', {'form': form })