from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .request_form_choices import *

User = get_user_model()

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    address1 = models.CharField("Address 1",max_length=1024)
    address2 = models.CharField("Address 2",max_length=1024, blank=True)
    city = models.CharField("City", max_length=255)
    zip_code = models.CharField("ZIP / Postal code",max_length=12)
    locations = models.CharField("Location",choices=CITY_CHOICES,max_length=1024)
    contact_preference = models.CharField(choices=CONTACT_CHOICES, max_length=150)
    agree_transfer = models.BooleanField(choices=AGREE_TRANSFER_CHOICES),
    #accept a list of items
    prefered_food = models.TextField(max_length=1024)
    items_list = models.TextField(max_length=2048)
    food_restrictions = models.TextField(default=None, blank=True, max_length=1024)
    household_number = models.SmallIntegerField("Family Size",default=1)
    urgency = models.CharField(choices=URGENCY_CHOICES, max_length=150)
    financial_support = models.CharField(choices=FINANCIAL_SUPPORT_CHOICES,max_length=150)
    special_info = models.TextField(blank=True, max_length=2048)
    share_info = models.BooleanField(choices=SHARE_INFO_CHOICES)
    need_checkin = models.CharField(choices=NEED_CHECKIN_CHOICES,max_length=150)
    extra_info = models.TextField(blank=True, max_length=1024)
    ma_pod_setup = models.BooleanField(choices=MAPOD_SETUP_CHOICES,max_length=150, default=None, blank=True)
    offer_resources = models.TextField(blank=True, max_length=1024)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=REQUEST_STATUS_CHOICES, max_length=150, default="New")
    last_edit = models.CharField("Last edit by",max_length=150)
    volunteer_status = models.CharField('Support Status',choices=VOLUNTEER_STATUS_CHOICES, max_length=150, default='Available')
    admin_notes = models.TextField(blank=True, null=True, max_length=1024)


    def __str__(self):
        return "#{} - {}".format(self.id, self.requester)


class Volunteer(models.Model):
    id = models.AutoField("Support ID", primary_key=True)
    supporter = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    status = models.CharField(choices=VOLUNTEERING_STATUS_CHOICES, max_length=150, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    admin_notes = models.TextField(blank=True, null=True, max_length=1024)

    def __str__(self):
        return "Support #{}".format(self.id)
    
    class Meta:
        verbose_name = 'Support'

