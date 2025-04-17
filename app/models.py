from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=32)
    qualification=models.CharField(max_length=32)
    gender=models.CharField(max_length=2)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=255)
    yop=models.DateField()
    course=models.CharField(max_length=40)
    skills=models.CharField(max_length=60)
    mock_rating=models.IntegerField()
    

