from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Comment, Reply
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','author', 'comment_content', 'request', 'is_approved', 'created_date')
    list_display_links = ('id',)
    list_filter = ('is_approved',)
    list_editable = ('comment_content','is_approved')
    search_fields = ('id','author','request')
    readonly_fields = ('request',)
    list_per_page = 25

admin.site.register(Comment, CommentAdmin)


