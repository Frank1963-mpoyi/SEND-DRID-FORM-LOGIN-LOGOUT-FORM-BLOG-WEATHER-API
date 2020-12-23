#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DescriptionSerializer
from .models import Description


class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Description.objects.all()
    # specify the serialize class we want to use
    serializer_class = DescriptionSerializer



