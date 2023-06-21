from django.db import models

# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=30)
    std_Roll=models.CharField(max_length=6)
    std_Email=models.EmailField(max_length=30)
    std_Dept=models.CharField(max_length=30)
    

class Teacher(models.Model):
    T_name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    Salary=models.IntegerField()  
    join_Date=models.DateField(max_length=30)
