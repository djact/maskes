from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from PIL import Image
from supports.models import Volunteer, Request
from io import BytesIO
from django.core.files import File
from pathlib import Path

User = get_user_model()

class Reimbursement(models.Model):
    volunteer = models.OneToOneField(Volunteer, on_delete=models.CASCADE, verbose_name = "Support ID")
    receipt_photo = models.ImageField(default=None, upload_to='receipt_photos/%Y/%m/%d/', null=True, blank=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(choices=(('In Process', 'In Process'),('Completed','Completed')), max_length=150, default=None)
    volunteer_notes = models.TextField(blank=True, null=True, max_length=1024)
    created_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.receipt_photo)       
        if img.height > 500 or img.width > 500:
            image_types = {
                'jpeg': 'JPEG',
                'jpg': 'JPEG',
                'png': 'PNG',
                'gif': 'GIF',
                'tif': 'TIFF',
            }
            buffer = BytesIO()
            image_path = Path(self.receipt_photo.name)
            image_filename = image_path.name
            filename_suffix = image_path.suffix[1:].lower()
            image_format = image_types[filename_suffix] 
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(buffer, format=image_format)
            file_object = File(buffer)
            file_object.content_type = 'image/jpeg'
            self.receipt_photo.save('{}-{}'.format(self.id, image_filename), file_object)
            self.save()
    
    def __str__(self):
        return '{} - {} - ${}'.format(self.id, self.volunteer.supporter.display_name, self.amount);

class Donation(models.Model):
    donator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Donator")
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name = "Request ID")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=150, default='unpaid')
    payment_id = models.CharField(max_length=40, blank=True, null=True)


    def __str__(self):
        return 'Donate Amount: {}'.format(self.amount);