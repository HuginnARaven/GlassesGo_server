from django.contrib import admin

from users.models import OrderPremade, OrderCustom

admin.site.register(OrderPremade)
admin.site.register(OrderCustom)
