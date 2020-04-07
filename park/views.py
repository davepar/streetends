from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from park.models import Park
from park.serializers import ParkSerializer

class ParkViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows parks to be viewed."""
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
