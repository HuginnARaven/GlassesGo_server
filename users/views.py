from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.serializers import OrderPremadeSerializer, OrderCustomSerializer
from users.models import OrderPremade, OrderCustom


class OrderPremadeView(mixins.CreateModelMixin, GenericViewSet):
    queryset = OrderPremade.objects.all()
    serializer_class = OrderPremadeSerializer


class OrderCustomView(mixins.CreateModelMixin, GenericViewSet):
    queryset = OrderCustom.objects.all()
    serializer_class = OrderCustomSerializer
