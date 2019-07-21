from rest_framework_gis.filters import DistanceToPointFilter


class DistanceFilter(DistanceToPointFilter):

    def filter_queryset(self, request, queryset, view):
        point = self.get_filter_point(request)
        if not point:
            return queryset

        queryset = view.queryset.filter(coverage_area__intersects=point)

        return super().filter_queryset(request, queryset, view)
