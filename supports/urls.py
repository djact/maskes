from django.urls import path, include
from rest_framework import routers
from .views import RequesterViewSet, VolunteerViewSet, VolunteeringViewSet

router = routers.DefaultRouter()
router.register(r'requester', RequesterViewSet, basename='requester')
router.register(r'volunteer', VolunteerViewSet, basename='volunteer')
router.register(r'volunteering', VolunteeringViewSet, basename='volunteering')


app_name = 'supports'

urlpatterns = [
    path('', include(router.urls)),
]
