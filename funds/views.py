from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import ReimbursementSerializer, DonationSerializer, DonationListSerializer
from .models import Reimbursement, Donation
from requests.models import Request, Volunteer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class ReimbursementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReimbursementSerializer
    queryset = Reimbursement.objects.all().order_by('-created_date')

class DonationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DonationSerializer
    queryset = Donation.objects.all().order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(donator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.updated_date = timezone.now()
        instance.save()


class ListDonationForSignleRequest(ListAPIView):
    serializer_class = DonationListSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        return Donation.objects.filter(request_id=self.kwargs.get('uid'))
    
    def list(self, request, uid):
        queryset = self.get_queryset(uid)
        serializer = DonationListSerializer(queryset, many=True)
        return Response(serializer.data)

    