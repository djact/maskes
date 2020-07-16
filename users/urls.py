from django.urls import path, include
from .views import CustomTokenObtainPairView

app_name='users'

urlpatterns = [
    path('auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('', include('djoser.urls')),
]
