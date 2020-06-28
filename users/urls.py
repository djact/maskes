from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]
