from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Comment, Reply
from django.urls import reverse
from django.utils.safestring import mark_safe
from requests.models import Volunteer
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','author', 'comment_content', 'request_link', 'support_link', 'volunteer_link', 'reviewed', 'created_date')
    list_display_links = ('id',)
    list_filter = ('is_approved','reviewed')
    list_editable = ('reviewed',)
    search_fields = ('id','author__first_name','author__last_name','comment_content')
    readonly_fields = ('request_link','volunteer_link','created_date')
    exclude = ('author',)
    list_per_page = 25

    def volunteer_link(self, obj):
        return mark_safe('<a href="http://localhost:3000/volunteer/{}/" target="_blank">View</a>'.format(obj.request.id))
    volunteer_link.short_description = 'Link'

    def request_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.request._meta.app_label,  obj.request._meta.model_name),  args=[obj.request.id] ),
            obj.request
        ))
    request_link.short_description = 'Request Info'

    def support_link(self, obj):
        try:
            support = Volunteer.objects.get(request=obj.request)
            return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (support._meta.app_label,  support._meta.model_name),  args=[support.id] ),
            support.status
            ))
        except:
            return None 
    support_link.short_description = 'Support Info'

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super().save_model(request, obj, form, change)
        

class ReplyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','author', 'comment_link', 'created_date')
    list_display_links = ('id',)
    search_fields = ('id',)
    readonly_fields = ('comment',)
    list_per_page = 25
    readonly_fields = ('created_date','comment_link')
    exclude = ('author',)

    def comment_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.comment._meta.app_label,  obj.comment._meta.model_name),  args=[obj.comment.id] ),
            obj.comment
        ))
    comment_link.short_description = 'Comment Link'

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)


