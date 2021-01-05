from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .serializers import CustomTokenObtainPairSerializer, ProfileSerializer

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly

from .models import UserProfile
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from djoser.views import UserViewSet

from djoser import signals
from djoser.conf import settings
from djoser.compat import get_user_email
from offers.models import Offer

class CustomUserViewSet(UserViewSet):
    def perform_create(self, serializer):
        data = self.request.data["volunteer_info"]
        user = serializer.save()
        Offer.objects.create(
            volunteer = user,
            contact_preference = data["contact_preference"],
            locations = data["locations"],
            phone = data["phone"],
            city = data["city"],
            zip_code = data["zip_code"],
            transportation_access = data["transportation_access"],
            walk_distance = data["walk_distance"],
            financial_support = data["financial_support"],
            special_info = data["special_info"],
            additional_supplies = data["additional_supplies"],
            need_checkin = data["need_checkin"],
            extra_info = data["extra_info"],
            ma_pod_setup = data["ma_pod_setup"],
            support_skills = data["support_skills"],
            accessibility_needs = data["accessibility_needs"],
            availability = data["availability"],
            volunteer_hours = data["volunteer_hours"],
            languages = data["languages"],
            coordinating = data["coordinating"],
            storage_space = data["storage_space"],
            pickup_concern = data["pickup_concern"],
        )
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        User = get_user_model()
        try:
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=request.data['email'])
            token, created = Token.objects.get_or_create(user=user)
            user_logged_in.send(sender=user.__class__, request=request, user=user)
            print(user.last_login)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        if self.action == 'list':
            return UserProfile.objects.filter(user=self.request.user)
        else:
            return UserProfile.objects.filter(user__is_volunteer__exact=True).order_by('-created_date')


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = [AllowAny,]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)