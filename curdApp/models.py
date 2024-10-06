from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    rollno= models.IntegerField()
    school = models.CharField(max_length=70)
    address = models.CharField(max_length=60)
