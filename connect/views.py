from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Comment, Reply
from requests.models import Request
from . import serializers

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all().order_by('-created_date')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CommentListSerializer
        return serializers.CommentDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['post'])
    def view_comments(self, request, pk=None):
        try:
            request_id = self.request.data['requestId']
            request = Request.objects.get(id=request_id)
            queryset = Comment.objects.filter(request=request).order_by('-created_date')
        except:
            queryset = Comment.objects.none()
        page = self.paginate_queryset(queryset)
        serializer = serializers.CommentListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    

class ReplyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Reply.objects.all().order_by('-created_date')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ReplyListSerializer
        return serializers.ReplyDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



       
            
       
        

