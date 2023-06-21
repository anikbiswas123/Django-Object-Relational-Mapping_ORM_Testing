from django.shortcuts import render
from .models import *
from datetimerange import data

# Create your views here.
def Home(request):
    # student_data=student.objects.all()
    # student_data=student.objects.filter(name__exact="sumilon") # exact query ja ta milba sa diba
    # student_data=student.objects.filter(name__iexact="Sumilon") exact query value na holo hoba
    
    # student_data=student.objects.filter(name__contains='n')  spcific letter daiye kona data utla aner janno containts user kora hoy
    
    # student_data=student.objects.filter(id__in=[1,3,5])
    # student_data=student.objects.filter(id__in=[2,4])
    
    # student_data=student.objects.filter(marks__in=[60,45])
    # student_data=student.objects.filter(marks__gt=40) #gt means greater then
    
    # student_data=student.objects.filter(marks__gte=60) #gt means greater then equal
    
    # student_data=student.objects.filter(marks__lt=60) #lt means less then 
    
    # student_data=student.objects.filter(marks__lte=45)  #lt means less then equail
    
    # student_data=student.objects.filter(name__startswith='R')
    # student_data=student.objects.filter(name__endswith='n')
    
    # student_data=student.objects.filter(marks__range=(35,60))
    
    student_data=student.objects.filter(pasdate__data__gt=data(''))
    
    
    
    
    
    print("Return",student_data)
    print("==========================")
    print(" SQl queryis ",student_data.query)
    return render(request,'Home.html',locals())