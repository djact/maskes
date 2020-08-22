from django.contrib import admin
from .models import UserProfile, UserAccount, UserAddress
# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'address1', 'address2','city','zip_code')
    list_filter = ('city',)
    search_fields = ('user__first_name','user__last_name','user__id')
class UserAccountAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name','id', 'email')
    list_display = ('id', 'first_name','last_name', 'email', 'is_volunteer', 'is_requester','is_staff')
    list_filter = ('is_staff','is_volunteer', 'is_requester')

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('phone','location','id', 'facebook','venmo', 'twitter',)
    list_display = ('id', 'user', 'phone', 'location', 'bio','created_date')
    list_filter = ('location',)


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress,UserAddressAdmin)

