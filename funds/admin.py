from django.contrib import admin
from .models import Reimbursement, Donation

from django.urls import reverse
from django.utils.safestring import mark_safe

class ReimbursementAdmin(admin.ModelAdmin):
    list_display = ('id','volunteer', 'request', 'supporter', 'total_cost', 'amount', 'status','created_date')
    list_display_links = ('id',)
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('id','volunteer__id',)
    readonly_fields = ('request','created_date')
    list_per_page = 25

    def request(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer.request._meta.app_label,  obj.volunteer.request._meta.model_name),  args=[obj.volunteer.request.id] ),
            obj.volunteer.request
        ))
    request.short_description = 'Request Info'

    def supporter(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer.supporter._meta.app_label,  obj.volunteer.supporter._meta.model_name),  args=[obj.volunteer.supporter.id] ),
            obj.volunteer.supporter
        ))
    supporter.short_description = 'Supporter Info'

    
admin.site.register(Reimbursement, ReimbursementAdmin);
admin.site.register(Donation);