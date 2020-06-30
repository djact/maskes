from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import RequestSerializer
from .models import Request
from .permissions import IsOwner, IsOwnerOrReadOnly

class RequestViewSet(ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(requester=self.request.user).order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)
