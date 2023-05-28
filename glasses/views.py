from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from rest_framework.viewsets import GenericViewSet

from glasses.models import MaterialColor, Material, Frame, Lens, LensColor, PremadeGlasses
from glasses.serializers import MaterialColorSerializer, MaterialSerializer, FrameSerializer, LensSerializer, \
    LensColorSerializer, PremadeGlassesSerializer


class MaterialColorViewSet(viewsets.ModelViewSet):
    queryset = MaterialColor.objects.all()
    serializer_class = MaterialColorSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class FrameViewSet(viewsets.ModelViewSet):
    queryset = Frame.objects.all()
    serializer_class = FrameSerializer


class LensViewSet(viewsets.ModelViewSet):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer


class LensColorViewSet(viewsets.ModelViewSet):
    queryset = LensColor.objects.all()
    serializer_class = LensColorSerializer


class PremadeGlassesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = PremadeGlasses.objects.all()
    serializer_class = PremadeGlassesSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'manufacturer']
