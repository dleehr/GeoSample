from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
from django.views.generic import RedirectView
from world.views import search_form


admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/search-form/')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^search-form/$', search_form)

)
