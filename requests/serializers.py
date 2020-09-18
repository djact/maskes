from rest_framework import serializers
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
        fields = ['id','requester', 'locations', 'household_number', 'urgency', 'items_list', 'food_restrictions', 'volunteer_status', 'created_date',
            'phone','address1','address2','city','zip_code', 'comments', 'reimbursement', 'delivery_status']
    
    def get_comments(self, obj):
        queryset = Comment.objects.filter(request=obj)
        comments = CommentDetailSerializer(queryset, many=True).data
        return [{comment['id']:comment['comment_content']} for comment in comments]

    def get_reimbursement(self, obj):
        try:
            volunteer = Volunteer.objects.get(request=obj)
            reimbursement = Reimbursement.objects.get(volunteer=volunteer)
            return ReimbursementSerializer(reimbursement).data
        except:
            return None

    def get_delivery_status(self, obj):
        try:
            volunteer = Volunteer.objects.get(request=obj)
            if volunteer.status == 'Delivered':
                return volunteer.status
            else:
                return 'On the way'
        except:
            return None

    

class VolunteerListSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField(read_only=True)

    def get_supporter(self, obj):
        try:
            volunteer = Volunteer.objects.get(request=obj)
            return {
                "display_name": volunteer.supporter.display_name,
                "id": volunteer.supporter.id,
            }
        except: 
            return None


    class Meta:
        model = Request
        fields = ['id','locations', 'household_number', 'urgency', 'items_list', 'volunteer_status', 'created_date', 'supporter']


class VolunteeringDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.email')
    request_detail = serializers.SerializerMethodField(read_only=True)
    reimbursement_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Volunteer
        fields = ['id','supporter','status','request','request_detail', 'reimbursement_detail', 'created_date']
    
    def get_request_detail(self, obj):
        request_detail = VolunteerDetailSerializer(obj.request).data
        return request_detail
    
    def get_reimbursement_detail(self, obj):
        try:
            queryset = Reimbursement.objects.get(volunteer=obj)
            reimbursement_detail = ReimbursementSerializer(queryset).data 
            return reimbursement_detail
        except:
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
    