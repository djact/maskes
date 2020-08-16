from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, ProfileSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

from .models import UserProfile
# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        if self.action == 'list':
            return UserProfile.objects.filter(user=self.request.user)
        else:
            return UserProfile.objects.filter(user__is_volunteer__exact=True).order_by('-created_date')