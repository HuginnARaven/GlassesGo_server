from django.urls import path, include
from rest_framework import routers


glasses_router = routers.SimpleRouter()


urlpatterns = [
    path('glasses/', include(glasses_router.urls)),
]
