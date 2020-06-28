from django.contrib import admin
from .models import UserProfile, UserAccount
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserProfile)

