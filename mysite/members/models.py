from django.db import models
from django.conf import settings

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True,blank=True)# we allow this field to be null
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='1')