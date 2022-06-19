from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from pyuploadcare.dj.models import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo =  CloudinaryField('profile_photos/', default='profile_photos/user')
    description = models.TextField()
    health_info = models.IntegerField(null=True, blank=True)
    health_officer = models.CharField(max_length=60, null=True, blank=True)
    police_info = models.IntegerField(null=True, blank=True)
    police_officer = models.CharField(max_length=60, null=True, blank=True)