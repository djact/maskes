from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from requests.models import Request, Volunteer
from .models import Reimbursement, Donation
from django.contrib.auth import get_user_model
User = get_user_model()


class ReimbursementSerializer(serializers.ModelSerializer):
    parser_classes = [MultiPartParser, FormParser]
    class Meta:
        model = Reimbursement
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    donator = serializers.ReadOnlyField(source='requester.first_name')
    class Meta:
        model = Donation
        fields = '__all__'

class DonationListSerializer(serializers.ModelSerializer):
    donator = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Donation
        fields = ["id","amount","updated_date", "status", "donator"]

    def get_donator(self, obj):
        try:
            donator = obj.donator
            return {
                "id": donator.id,
                "display_name": donator.display_name,
                "avatar": donator.userprofile.image.url,
            }
        except: 
            return None
    