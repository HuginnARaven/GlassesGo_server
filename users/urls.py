from django.urls import path, include
from rest_framework import routers

from users.views import OrderPremadeView, OrderCustomView

user_router = routers.SimpleRouter()
user_router.register(r'order-premade', OrderPremadeView, basename='order-premade')
user_router.register(r'order-custom', OrderCustomView, basename='order-custom')

urlpatterns = [
    path('user/', include(user_router.urls)),
]
