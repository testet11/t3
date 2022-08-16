import imp
from django.db import models
from django.utils.timezone import now
# Create your models here.

class fi(models.Model):  
    a = models.TextField(default="")
    b = models.TextField(default="")
    c = models.TextField(default="")
    d = models.TextField(default="")
    e = models.TextField(default="")
    f = models.TextField(default="")
    date = models.DateField(default=now)
