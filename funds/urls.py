from django.urls import path, include
from rest_framework import routers
from .views import ReimbursementViewSet

router = routers.DefaultRouter()
router.register(r'reimbursement', ReimbursementViewSet, basename='reimbursement')

app_name = 'funds'

urlpatterns = [
    path('', include(router.urls)),
]
