from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
# def home(request):
    # student_data= Student.objects.all()
    
    # student_data=Student.objects.filter(std_Roll=23)
    
    # student_data=Student.objects.exclude(std_Roll=21)
    
    # student_data=Student.objects.order_by("std_name")
    
    # student_data=Student.objects.order_by('-std_name')
    
    # student_data=Student.objects.order_by('?')
    
    # student_data=Student.objects.order_by('id').reverse()[:2] 
    
    # student_data=Student.objects.order_by('id').reverse()
    
    # amer django all() method use kora queryset anie but values() method use kora sa kaj ta para ji
    # student_data=Student.objects.values()
    
    # values() method sepacific method pass kora ji
    # student_data=Student.objects.values('std_Roll','std_Dept')
    
    # Jodie duplicate value thika 
    # Student_data=Student.objects.distinct()
    
    # student_data=Student.objects.values_list('id','std_name')
    # student_data=Student.objects.values_list('id','std_name',named=False)
    # student_data=Student.objects.values_list('id','std_name',named=True)
    
    # student_data=Student.objects.all()
    
    # student_data=Student.objects.using('default')
    
    #data field show the dataes
    # student_data=Student.objects.dates('id','std_name',named=True)
    
    
    #=============== Second table data include===========
    
    # q1=Student.objects.values_list('id','std_name',named=True)
    # q2=Teacher.objects.values_list('id','T_name',named=True)
    
    # student_data=q1.union(q2)
    
    # q1=Student.objects.values_list('id','std_name',named=True)
    # q2=Teacher.objects.values_list('id','T_name',named=True)
    
    # student_data=q1.union(q2,all=True)
    
    # q1=Student.objects.values_list('id','std_name',named=True)
    # q2=Teacher.objects.values_list('id','T_name',named=True)
    
    # student_data=q1.intersection(q2)
    
     
    # q1=Student.objects.values_list('id','std_name',named=True)
    # q2=Teacher.objects.values_list('id','T_name',named=True)
    
    # student_data=q1.difference(q2)
    
    
    #================= And or operations   ==================
    # student_data=Student.objects.filter(id=5) & Student.objects.filter(std_Roll=30)
    # student_data=Student.objects.filter(id=6,std_name="Anik biswas")
    # student_data=Student.objects.filter(Q(id=6) & Q(std_name="Anik biswas"))
    
    # student_data=Student.objects.filter(id=5) | Student.objects.filter(std_Roll=565)
    
    
    
    
    
    # print(student_data)
    # print("=========")
    # print("Sql Query", student_data.query)
    
    # return render(request,'Home.html',locals())
