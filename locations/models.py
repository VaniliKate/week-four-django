from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from pyuploadcare.dj.models import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.