from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import (RequesterDetailSerializer, RequesterListSerializer,
                            VolunteerDetailSerializer, VolunteerListSerializer,
                                VolunteeringDetailSerializer, VolunteeringListSerializer,)
from .models import Request, Volunteer
from .permissions import IsOwner, IsOwnerOrReadOnly, IsVolunteerOnly

class RequesterViewSet(ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RequesterListSerializer
        return RequesterDetailSerializer

    def get_queryset(self):
        return Request.objects.filter(requester=self.request.user).order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

class VolunteerViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsVolunteerOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return VolunteerListSerializer
        return VolunteerDetailSerializer
    
    def get_queryset(self):
        if self.request.user.is_volunteer:
            return (Request.objects.filter(status='In Process') | Request.objects.filter(status='Completed')).order_by('volunteer_status','-created_date')
        else: return None

    def post(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())
     
        search_values = self.request.data
        
        date = search_values['date']
        if date == 'oldest':
            queryset = queryset.order_by('created_date')

        location = search_values['location']
        
        if location != '':
            queryset = queryset.filter(locations__iexact=location)

        urgent = search_values['urgent']
        if urgent != '':
            queryset = queryset.filter(urgency__iexact=urgent)
        
        try:
            household_number = int(search_values['familySize'])
            if household_number != 0:
                if household_number >= 8:
                    queryset = queryset.filter(household_number__gte=household_number)
                else:
                    queryset = queryset.filter(household_number=household_number)
        except:
            pass
        
        request_no = search_values['requestId']
        if request_no != '':
            queryset = queryset.filter(id__iexact=request_no)
        
        #pagination
        page = self.paginate_queryset(queryset)
        serializer = VolunteerListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class VolunteeringViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsVolunteerOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return VolunteeringListSerializer
        return VolunteeringDetailSerializer
    
    def get_queryset(self):
        return Volunteer.objects.filter(supporter=self.request.user).order_by('-created_date')
    
    def perform_create(self, serializer):
        request = serializer.validated_data.get('request')
        request.volunteer_status = 'Unavailable'
        request.save()
        try:
            instance = Volunteer.objects.get(request=request,supporter=self.request.user)
            serializer.update(instance, validated_data)
        except:
            serializer.save(supporter=self.request.user, status="Signed Up")
    
    def perform_update(self, serializer):
        request = serializer.validated_data.get('request')
        status = serializer.validated_data.get('status')
        if status == 'Delivered':
            request.status = "Completed"
        else:
            request.status = "In Process"
        request.save()
        serializer.save()
        
    def perform_destroy(self, instance):
        request = instance.request
        request.volunteer_status = 'Available'
        request.save()
        instance.delete()

        

    

    
