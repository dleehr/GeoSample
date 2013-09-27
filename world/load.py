import os
from django.contrib.gis.utils import LayerMapping
from models import WorldBorder

# This dict provides a mapping of fields in the model to fields
# in the TM_WORLD_BORDERS-0.3.shp file containing layers
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
	}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))

def run(verbose=True):
	# args are model name, source file, and mapping dict
	# Transform is false because the database format is SRID 4326, which is WGS84,
	# and the shape file is already in this format
	lm = LayerMapping(WorldBorder, world_shp, world_mapping,
					  transform=False, encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)