from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model
from requests.models import Volunteer

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['first_name'] = self.user.first_name
        data['user_id'] = self.user.id
        data['is_volunteer'] = self.user.is_volunteer
        data['is_requester'] = self.user.is_requester
        return data

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    display_name = serializers.ReadOnlyField(source='user.display_name')

    volunteer_count = serializers.SerializerMethodField()
    delivered_count = serializers.SerializerMethodField()

    def get_volunteer_count(self, obj):
        count = Volunteer.objects.filter(supporter=obj.user).count()
        return count
    
    def get_delivered_count(self,obj):
        count = Volunteer.objects.filter(supporter=obj.user).filter(status="Delivered").count()
        return count

    class Meta:
        model = UserProfile
        fields = "__all__"
        lookup_field = "user_id"

class EmptySerializer(serializers.Serializer):
    pass