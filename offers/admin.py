from django.contrib import admin
from .models import Offer
from django.db import models
from django.forms import TextInput, Textarea
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe

class OfferAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id', 'last_edit','supporter_link','phone','city','created_date', 'locations')
    list_display_links = ('id',)
    list_filter = ('city', )

    search_fields = ('id','volunteer__first_name','volunteer__last_name','phone','city','zip_code','locations')
    list_per_page = 25
    readonly_fields = ('id','supporter_link', 'created_date')

    def supporter_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.volunteer._meta.app_label,  obj.volunteer._meta.model_name),  args=[obj.volunteer.id] ),
            obj.volunteer
        ))
    supporter_link.short_description = 'Volunteer Info'

    def save_model(self, request, obj, form, change):
        if change and request.user.is_staff:
            month = str(timezone.now().month)
            day = str(timezone.now().day)
            admin = request.user.first_name
            obj.last_edit = "{}-{} by {}".format(month,day,admin)
        obj.save()

admin.site.register(Offer, OfferAdmin)