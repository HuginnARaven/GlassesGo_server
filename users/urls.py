from django.urls import path, include
from rest_framework import routers


user_router = routers.SimpleRouter()


urlpatterns = [
    path('user/', include(user_router.urls)),
]
