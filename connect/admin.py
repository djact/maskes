from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Comment, Reply
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','author', 'comment_content', 'volunteer_link', 'reviewed', 'created_date')
    list_display_links = ('id',)
    list_filter = ('is_approved','reviewed')
    list_editable = ('reviewed',)
    search_fields = ('id','author','request')
    readonly_fields = ('request','volunteer_link')
    list_per_page = 25

    def volunteer_link(self, obj):
        return mark_safe('<a href="http://localhost:3000/volunteer/{}/" target="_blank">View</a>'.format(obj.request.id))
    volunteer_link.short_description = 'Volunteer Link'

class ReplyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','author', 'comment', 'created_date')
    list_display_links = ('id',)
    search_fields = ('id',)
    readonly_fields = ('comment',)
    list_per_page = 25

admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)


