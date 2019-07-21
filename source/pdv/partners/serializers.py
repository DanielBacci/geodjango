from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometryField
)

from pdv.partners.models import Partner


class PartnerSerializer(GeoFeatureModelSerializer):

    address = GeometryField()
    coverage_area = GeometryField()

    class Meta:
        model = Partner
        fields = '__all__'
        geo_field = 'address'
