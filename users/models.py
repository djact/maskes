from django.db import models
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        BaseUserManager)

class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name) #create a new model object
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

class UserAccount(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Account'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class UserProfile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()

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
