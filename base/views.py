from base.models import Glucose
from base.serializers import GlucoseSerializer
from rest_framework import viewsets, filters

class GlucoseViewSet(viewsets.ModelViewSet):
    serializer_class = GlucoseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['gerate_zeitstempel']
    queryset = Glucose.objects.all()

    def get_queryset(self) :
        queryset = self.queryset
        start = self.request.query_params.get('start')
        stop = self.request.query_params.get('stop')
        user_id = self.request.query_params.get('user_id')
        if start:
            queryset = queryset.filter(gerate_zeitstempel__gte=start)
        if stop:
            queryset = queryset.filter(gerate_zeitstempel__lte=stop)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset