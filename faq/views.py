from rest_framework.generics import ListAPIView
from .serializers import FAQSerializer
from .models import FAQ
from rest_framework.permissions import AllowAny
# Create your views here.

class FAQListView(ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    permission_classes = [AllowAny,]
