from django.urls import path, include
from rest_framework import routers

from glasses.views import MaterialColorViewSet, MaterialViewSet, FrameViewSet, LensViewSet, LensColorViewSet, \
    PremadeGlassesViewSet

glasses_router = routers.SimpleRouter()
glasses_router.register(r'material-color', MaterialColorViewSet, basename='material-color')
glasses_router.register(r'material', MaterialViewSet, basename='material')
glasses_router.register(r'frame', FrameViewSet, basename='frame')
glasses_router.register(r'lens', LensViewSet, basename='lens')
glasses_router.register(r'lens-color', LensColorViewSet, basename='lens-color')
glasses_router.register(r'premade-glasses', PremadeGlassesViewSet, basename='premade-glasses')


urlpatterns = [
    path('glasses/', include(glasses_router.urls)),
]
