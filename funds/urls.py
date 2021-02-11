from django.urls import path, include
from rest_framework import routers
from .views import ReimbursementViewSet, DonationViewSet, ListDonationForSignleRequest

router = routers.DefaultRouter()
router.register(r'reimbursement', ReimbursementViewSet, basename='reimbursement')
router.register(r'donation', DonationViewSet, basename='donation')

app_name = 'funds'

urlpatterns = [
    path('', include(router.urls)),
    path('donation-list/<int:uid>/', ListDonationForSignleRequest.as_view(), name='donationlist'),
]
