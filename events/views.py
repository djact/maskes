from rest_framework.generics import ListAPIView
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import AllowAny


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]