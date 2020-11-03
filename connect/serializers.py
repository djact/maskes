from rest_framework import serializers
from requests.models import Request
from .models import Comment, Reply

from django.contrib.auth import get_user_model
User = get_user_model()

class CommentUserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id', 'email']
    

class ReplyListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', "reply_content", "author", "author_name","created_date", "comment"]
    
    def get_author_name(self, obj):
        user = User.objects.get(id=obj.author.id)
        return user.display_name
    
class ReplyDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(read_only=True)
    author_image = serializers.SerializerMethodField(source='get_absolute_url')

    class Meta:
        model = Reply
        fields = '__all__'

    def get_author_name(self, obj):
        user = User.objects.get(id=obj.author.id)
        return user.display_name
    
    def get_author_image(self, obj):
        # use context build_absolute_uri on custom view_replies
        return self.context.get('request').build_absolute_uri(obj.author.userprofile.image.url)

class CommentListSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField(read_only=True)
    author_image = serializers.SerializerMethodField(source='get_absolute_url')
    replies = ReplyListSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_reply_count(self, obj):
        count = Reply.objects.filter(comment=obj).count()
        return count
    
    def get_author_name(self, obj):
        user = User.objects.get(id=obj.author.id)
        return user.display_name
    
    def get_author_image(self, obj):
        # use context build_absolute_uri on custom view_comments
        return self.context.get('request').build_absolute_uri(obj.author.userprofile.image.url)
        
    
    def get_replies(self, obj):
        queryset = Reply.objects.filter(comment=obj)
        replies = ReplyListSerializer(queryset, many=True).data
        return replies

class CommentDetailSerializer(serializers.ModelSerializer):
    replies = ReplyListSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id','request','comment_content', 'author', 'replies']
    
    def get_replies(self, obj):
        queryset = Reply.objects.filter(comment=obj)
        replies = ReplyListSerializer(queryset, many=True).data
        return replies


class EmptySerializer(serializers.Serializer):
    pass