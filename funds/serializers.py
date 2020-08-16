from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from requests.models import Request, Volunteer
from .models import Reimbursement
from django.contrib.auth import get_user_model
User = get_user_model()


class ReimbursementSerializer(serializers.ModelSerializer):
    parser_classes = [MultiPartParser, FormParser]
    class Meta:
        model = Reimbursement
        fields = '__all__'