from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = (('General', 'General'), ('Requesting Support', 'Requesting Support'),
                        ('Offering Support', 'Offering Support'), ('Using the App', 'Using the App'))
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Categories'


class FAQ(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'FAQ'