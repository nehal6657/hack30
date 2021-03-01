from django.db import models


<<<<<<< HEAD
# Create your models here.


class destination(models.Model):
  
    Total = models.IntegerField()
    quarantine = models.IntegerField()
    room = models.IntegerField()
    num_quarantine = models.IntegerField()
    num_free = models.IntegerField()
    start = models.DateTimeField()
    
    
=======
class Student(models.Model):
    name: models.CharField(max_length=150)
    rollno: models.CharField()
    location: models.CharField()

>>>>>>> eac7e668bda762ef93b5c2e650983a5f05b99547
