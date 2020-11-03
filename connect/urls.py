from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet, ReplyViewSet

app_name = 'connect'

router = routers.DefaultRouter(trailing_slash=True)

router.register('comments', CommentViewSet, basename='comment')
router.register('replies', ReplyViewSet, basename='reply')

urlpatterns = [
    path('', include(router.urls)),
]
