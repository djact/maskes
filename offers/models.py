from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .offer_form_choices import *

User = get_user_model()

class Offer(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_preference = models.CharField(choices=CONTACT_CHOICES, max_length=100)
    phone = models.CharField(max_length=20)
    city = models.CharField("City", max_length=35)
    zip_code = models.CharField("ZIP / Postal code",max_length=15)
    transportation_access = models.CharField(max_length=15)
    walk_distance = models.CharField(blank=True, max_length=200)
    special_info = models.TextField(blank=True, max_length=2048)
    additional_supplies = models.CharField(blank=True, max_length=15)
    extra_info = models.TextField(blank=True, max_length=1024)
    support_skills = models.TextField(max_length=1024)
    volunteer_hours = models.CharField(max_length=5)
    languages = models.CharField(blank=True, max_length=200)
    storage_space = models.CharField(blank=True, max_length=200)
    pickup_concern = models.CharField(blank=True, max_length=200)

    created_date = models.DateTimeField(default=timezone.now)
    last_edit = models.CharField("Last edit by",max_length=150)
    admin_notes = models.TextField(blank=True, null=True, max_length=1024)

    locations = models.CharField("Location",max_length=250)
    financial_support = models.CharField(blank=True ,max_length=150)
    need_checkin = models.CharField(blank=True,max_length=150)
    ma_pod_setup = models.CharField(blank=True,max_length=150, default=None)
    accessibility_needs = models.CharField(blank=True, max_length=150)
    availability = models.CharField(blank=True, max_length=150)
    coordinating = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return '{} - {} {}'.format(self.volunteer.id, self.volunteer.first_name, self.volunteer.last_name)

