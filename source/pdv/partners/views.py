from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

from pdv.partners.filters import DistanceFilter
from pdv.partners.models import Partner
from pdv.partners.serializers import PartnerSerializer


class PartnersViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing partners instances.
    """
    serializer_class = PartnerSerializer
    pagination_class = GeoJsonPagination
    queryset = Partner.objects.all()
    filter_backends = (DistanceFilter,)
    distance_filter_field = 'address'
