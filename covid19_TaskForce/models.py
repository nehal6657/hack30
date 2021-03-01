from django.db import models


# Create your models here.


class destination(models.Model):
  
    Total = models.IntegerField()
    quarantine = models.IntegerField()
    room = models.IntegerField()
    num_quarantine = models.IntegerField()
    num_free = models.IntegerField()
    start = models.DateTimeField()
    
    
