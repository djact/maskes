from django.contrib import admin
from .models import Request, Volunteer
from django.forms import TextInput, Textarea
from django.db import models
from django.utils import timezone

class RequestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','created_date', 'last_edit', 'status','requester','phone','city','items_list','urgency',)
    list_display_links = ('id',)
    list_filter = ('status','city')
    list_editable = ('status','items_list')
    search_fields = ('requester__first_name','requester__last_name','phone','address1','city','zip_code',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if change and request.user.is_staff:
            month = str(timezone.now().month)
            day = str(timezone.now().day)
            admin = request.user.first_name
            obj.last_edit = "{}-{} by {}".format(month,day,admin)
        obj.save()

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer)
