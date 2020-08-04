from django.db import models
from django.utils import timezone
from requests.models import Request
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Comment(models.Model):
    request = models.ForeignKey(Request,on_delete = models.CASCADE,related_name="comments")
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    comment_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=True, verbose_name='Approved')

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_content

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reply_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=True, verbose_name='Approved')

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'Replies'

    def __str__(self):
        return self.reply_content