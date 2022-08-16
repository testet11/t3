import imp
from django.db import models
from django.utils.timezone import now
# Create your models here.

class fi(models.Model): 
    body = models.TextField()
    date = models.DateField(default=now)