from rest_framework import serializers

from users.models import OrderPremade, OrderCustom


class OrderPremadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPremade
        fields = "__all__"


class OrderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCustom
        fields = "__all__"