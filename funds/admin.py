from django.contrib import admin
from .models import Reimbursement, Donation

from django.urls import reverse
from django.utils.safestring import mark_safe

class ReimbursementAdmin(admin.ModelAdmin):
    list_display = ('id','volunteer_link', 'request', 'supporter', 'total_cost', 'amount', 'status','created_date')
    list_display_links = ('id',)
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('id','volunteer__id',)
    readonly_fields = ('request','created_date', 'supporter','volunteer_link','supporter_venmo')
    list_per_page = 25

    def request(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer.request._meta.app_label,  obj.volunteer.request._meta.model_name),  args=[obj.volunteer.request.id] ),
            obj.volunteer.request
        ))
    request.short_description = 'Request Info'

    def supporter(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer.supporter.userprofile._meta.app_label,  obj.volunteer.supporter.userprofile._meta.model_name),  args=[obj.volunteer.supporter.userprofile.id] ),
            obj.volunteer.supporter
        ))
    supporter.short_description = 'Supporter Info'

    def supporter_venmo(self, obj):
        return mark_safe('<a href="{}"> {}</a>'.format(
            'https://venmo.com/{}'.format(obj.volunteer.supporter.userprofile.venmo),
            obj.volunteer.supporter.userprofile.venmo,
        ))
    supporter_venmo.short_description = 'Supporter Venmo'

    def volunteer_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer._meta.app_label,  obj.volunteer._meta.model_name),  args=[obj.volunteer.id] ),
            obj.volunteer
        ))
    volunteer_link.short_description = 'Support Info'

    
admin.site.register(Reimbursement, ReimbursementAdmin);
admin.site.register(Donation);