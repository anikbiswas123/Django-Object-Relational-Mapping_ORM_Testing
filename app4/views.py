from django.shortcuts import render
from app.models import *

# Create your views here.

def Home(request):
    
    student_data=Student.objects.all()
    average=student_data.aggregate(Avg('marks'))
    
    print("Return",student_data)
    print("==========================")
    print(" SQl queryis ",student_data.query)
    return render(request,'Home.html',locals())
