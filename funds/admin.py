from django.contrib import admin
from .models import Reimbursement

class ReimbursementAdmin(admin.ModelAdmin):
    list_display = ('id','volunteer', 'total_cost', 'amount', 'status','created_date')
    list_display_links = ('id',)
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('id','volunteer__id',)
    list_per_page = 25
    pass

admin.site.register(Reimbursement, ReimbursementAdmin);