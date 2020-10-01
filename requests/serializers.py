from rest_framework import serializers
from .request_form_choices import (
    VOLUNTEERING_STATUS_SIGNED_UP, 
    VOLUNTEERING_STATUS_READY, 
    VOLUNTEERING_STATUS_DELIVERED,REQUEST_STATUS_CHOICES,
    VOLUNTEERING_STATUS_OTW)
    
from .models import Request, Volunteer
from django.contrib.auth import get_user_model
from funds.serializers import ReimbursementSerializer
from funds.models import Reimbursement
from connect.models import Comment, Reply
from connect.serializers import CommentDetailSerializer, CommentListSerializer
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
    comments = serializers.SerializerMethodField()
    requester = serializers.ReadOnlyField(source='requester.first_name')
    reimbursement = serializers.SerializerMethodField()
    delivery_status = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['id','requester', 'locations', 
            'household_number', 'urgency', 'items_list', 
            'food_restrictions', 'volunteer_status', 'created_date',
            'phone','address1','address2','city','zip_code', 
            'comments', 'reimbursement', 'delivery_status']
    
    def get_comments(self, obj):
        queryset = Comment.objects.filter(request=obj)
        comments = CommentDetailSerializer(queryset, many=True).data
        return [{comment['id']:comment['comment_content']} for comment in comments]

    def get_reimbursement(self, obj):
        try:
            reimbursement = Reimbursement.objects.get(volunteer=obj.volunteer)
            return ReimbursementSerializer(reimbursement).data
        except (
            Reimbursement.DoesNotExist, 
            Request.volunteer.RelatedObjectDoesNotExist
        ): return None

    def get_delivery_status(self, obj):
        if Volunteer.objects.filter(request=obj).exists():
            volunteer = Volunteer.objects.get(request=obj)
            return volunteer.status if(
                 volunteer.status == VOLUNTEERING_STATUS_DELIVERED
                 ) else VOLUNTEERING_STATUS_OTW
        else: 
            return None
    

class VolunteerListSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField(read_only=True)

    def get_supporter(self, obj):
        if Volunteer.objects.filter(request=obj).exists():
            volunteer = Volunteer.objects.get(request=obj)
            return {
                "display_name": volunteer.supporter.display_name,
                "id": volunteer.supporter.id,
            }
        else: 
            return None

    class Meta:
        model = Request
        fields = ['id','locations', 'household_number', 
            'urgency', 'items_list', 'volunteer_status', 
            'created_date', 'supporter']


class VolunteeringDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.email')
    request_detail = serializers.SerializerMethodField(read_only=True)
    reimbursement_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Volunteer
        fields = ['id','supporter','status','request',
            'request_detail', 'reimbursement_detail', 
            'created_date', 'skip_reimbursement']
    
    def get_request_detail(self, obj):
        request_detail = VolunteerDetailSerializer(obj.request).data
        return request_detail
    
    def get_reimbursement_detail(self, obj):
        if Reimbursement.objects.filter(volunteer=obj).exists():
            reimbursement = Reimbursement.objects.get(volunteer=obj)
            reimbursement_detail = ReimbursementSerializer(reimbursement).data 
            return reimbursement_detail
        else:
            return None
    
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
    