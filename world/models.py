from django.contrib.gis.db import models

class WorldBorder(models.Model):
	# Regular Django Fields corresponding to the attributes in the world borders shapefile
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField('Population 2005')
	fips = models.CharField('FIPS Code', max_length=2)
	iso2 = models.CharField('2 Digit ISO', max_length=2)
	iso3 = models.CharField('3 Digit ISO', max_length=3)
	un = models.IntegerField('United Nations Code')
	region = models.IntegerField('Region Code')
	subregion = models.IntegerField('Sub-Region Code')
	lon = models.FloatField()
	lat = models.FloatField()
	# That's it for boring old django models
	# Geodjango-speciic: a geometry fields and overriding the manager with a GeoManager
	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

	def __unicode__(self):
		return self.name

