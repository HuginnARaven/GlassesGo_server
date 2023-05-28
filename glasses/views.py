from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from glasses.models import MaterialColor, Material, Frame, Lens, LensColor
from glasses.serializers import MaterialColorSerializer, MaterialSerializer, FrameSerializer, LensSerializer, \
    LensColorSerializer


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
