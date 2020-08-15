from django.urls import path, include
from rest_framework import routers
from .views import CustomTokenObtainPairView, ProfileViewSet

app_name='users'

router = routers.DefaultRouter(trailing_slash=True)
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
]
