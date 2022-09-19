# from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class WorldBorder(models.Model):
    name = models.CharField(max_length=50,
                            null=True)
    area = models.IntegerField(null=True)
    pop2005 = models.IntegerField("Population 2005",
                                  null=True)
    fips = models.CharField("FIPS Code",
                            max_length=2,
                            null=True)
    iso2 = models.CharField("2 Digit ISO",
                            max_length=2,
                            null=True)
    iso3 = models.CharField("3 Digit ISO",
                            max_length=3,
                            null=True)
    un = models.IntegerField("united Nation Code",
                             null=True)
    region = models.IntegerField("Region Code",
                                 null=True)
    subregion = models.IntegerField("Sub Region Code",
                                    null=True)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    # """ Geometry field"""
    # mpoly = models.MultiPolygonField(null=True)
    #
    # def __str__(self):
    #     return self.name

    geom = models.MultiPolygonField(srid=4326,
                                    null=True)

    """ Auto-generated LayerMapping dictionary for worldBordr model"""
    worldborder_mapping = {
        "fips": "FIPS",
        "iso2": "ISO2",
        "iso3": "ISO3",
        "un": "UN",
        "name": "NAME",
        "area": "AREA",
        "pop2005": "POP2005",
        "region": "REGION",
        "subregion": "SUBREGION",
        "lon": "LON",
        "lat": "LAT",
        "geom": "MULTIPOLYGON",
    }
