from rest_framework import serializers
from .models import Request, Volunteer
from django.contrib.auth import get_user_model
User = get_user_model()

class RequesterDetailSerializer(serializers.ModelSerializer):
    requester = serializers.HyperlinkedRelatedField(
        view_name='users:useraccount-detail',
        read_only=True,
    )
    name = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    
    class Meta:
        model = Request
        exclude = ['last_edit']

    def get_name (self, obj):
        return obj.requester.first_name

class RequesterListSerializer(serializers.ModelSerializer):
    requester = serializers.HyperlinkedRelatedField(
        view_name='users:useraccount-detail',
        read_only=True,
    )
    name = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    
    class Meta:
        model = Request
        fields = ['id','requester', 'name', 'status', 'items_list', 'created_date']

    def get_name (self, obj):
        return obj.requester.first_name

class VolunteerDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Request
        fields = ['id','locations', 'household_number', 'urgency', 'items_list', 'food_restrictions', 'volunteer_status', 'created_date']
    

class VolunteerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','locations', 'household_number', 'urgency', 'volunteer_status', 'created_date']


class VolunteeringDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.email')
    request_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Volunteer
        fields = ['id','supporter','status','request','request_detail', 'created_date']
    
    def get_request_detail(self, obj):
        request_detail = VolunteerDetailSerializer(obj.request).data
        return request_detail
    
class VolunteeringListSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.first_name')
    request_info = serializers.SerializerMethodField(read_only=True)
    status = serializers.ReadOnlyField()
    
    class Meta:
        model = Volunteer
        fields = ['id','supporter','status','request','request_info', 'created_date']

    def get_request_info(self, obj):
        request_info = VolunteerListSerializer(obj.request).data
        return request_info
    