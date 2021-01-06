from django.urls import path
from .views import EventList

app_name = 'events'

urlpatterns = [
    path('', EventList.as_view(), name='event'),
]
