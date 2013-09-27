# Create your views here.
from django.contrib.gis.geos.point import Point
from django.contrib.gis.measure import Distance
from django.core.exceptions import ObjectDoesNotExist

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
			try:
				feature  = WorldBorder.objects.get(mpoly__intersects=cd['point'])
			except ObjectDoesNotExist:
				feature = None
			# Also find things say, within 100 miles?
			nearby= WorldBorder.objects.filter(mpoly__distance_lte=(cd['point'], Distance(mi=1000))).distance(cd['point']).order_by('distance')
			response_dict = {'feature': feature, 'nearby': nearby}
			return render(request, 'search_results.html', response_dict)

	else:
		form = SearchForm
		# gis/openlayers-osm.html?
		return render(request, 'search_form.html', {'form': form })