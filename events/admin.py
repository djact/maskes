from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display_links = ('id','title')
    list_display = ('id','title', 'description')
    search_fields = ('id','title',)
    list_per_page = 25

admin.site.register(Event, EventAdmin)
