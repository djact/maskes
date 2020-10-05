from django.db import models
from PIL import Image
from django.utils import timezone
from requests.request_form_choices import CITY_CHOICES
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        BaseUserManager)

class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, 
        password=None, display_name=None, is_requester=False, is_volunteer=False):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name,
            display_name=display_name,
            is_volunteer=is_volunteer,
            is_requester=is_requester) 
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, 
        password, display_name):
        user = self.create_user(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
            display_name=display_name,
            is_requester = True,
            is_volunteer = True)
        user.is_superuser = True
        user.is_staff = True
        user.save()

class UserAccount(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    display_name = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_requester = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'display_name']

    class Meta:
        verbose_name = 'Account'

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.email.split('@')[0]
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class UserAddress(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE )
    address1 = models.CharField("Address 1",max_length=1024)
    address2 = models.CharField("Address 2",max_length=1024)
    city = models.CharField("City",max_length=1024)
    zip_code = models.CharField("ZIP / Postal code",max_length=12)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    
    def __str__(self):
        return "{} - {} {}, {}, WA{}".format(self.user, self.address1, self.address2, self.city, self.zip_code)

class UserProfile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=25, blank=True)
    facebook = models.CharField(max_length=25, blank=True)
    twitter = models.CharField(max_length=25, blank=True)
    venmo = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    fullname_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)
    phone_privacy = models.BooleanField(default=True)
    location_privacy = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.email.split('@')[0]
    #Profile Photo square crop
    def crop_center(self, image, crop_width, crop_height):
        width, height = image.size
        return image.crop(((width - crop_width) // 2,
                            (height - crop_height) // 2,
                            (width + crop_width) // 2,
                            (height + crop_height) // 2))

    def crop_max_square(self, image):
        return self.crop_center(image, min(image.size), min(image.size))

    # RESIZE image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)       
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img = self.crop_max_square(img).resize(output_size, Image.LANCZOS)
            img.save(self.image.path, quality=95)
