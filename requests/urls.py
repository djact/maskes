from django.urls import path, include
from rest_framework import routers
from .views import RequestViewSet

router = routers.DefaultRouter()
router.register(r'', RequestViewSet, basename='request')

app_name = 'requests'

urlpatterns = [
    path('', include(router.urls)),
]
