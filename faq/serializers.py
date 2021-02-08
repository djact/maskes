from rest_framework.serializers import Serializer
from .models import FAQ

class FAQSerializer(Serializer):
    class Meta:
        model = FAQ
        fields = '__all__'
