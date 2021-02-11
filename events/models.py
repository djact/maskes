from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    content = RichTextField()
    event_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title