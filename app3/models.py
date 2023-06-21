from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    Roll=models.IntegerField()
    city=models.CharField(max_length=30)
    marks=models.IntegerField()
    pasdate=models.DateField()
    admDateTime=models.DateTimeField()
