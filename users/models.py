from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    # user_id = models.CharField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15) 
    address = models.TextField()
    city = models.CharField(max_length=100) 
    state = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    pincode = models.CharField(max_length=10)
    profile_image = models.ImageField( upload_to="profiles/", null=True, blank=True ) 
    date_of_birth = models.DateField(null=True, blank=True) 
    gender = models.CharField(max_length=20)
    
    
