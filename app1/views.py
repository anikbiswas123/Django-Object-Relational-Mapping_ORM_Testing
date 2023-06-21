from django.shortcuts import render
from app.models import *


# Create your views here.
def home(request):

    # student_data=Student.objects.get(pk=1)
    # student_data=Student.objects.get(std_name="Rupa")
    
    # student_data=Student.objects.first()
    
    # student_data=Student.objects.last()
    
    # student_data=Student.objects.order_by('-std_name').first()
    
    # student_data=Student.objects.latest()
    # student_data=Student.objects.earliest()
    
    # student_data=Student.objects.all()
    
    # print(student_data.exists())
    
    # student_data=Student.objects.create(std_name='Sohan',std_Roll=45,std_Email="Shohan@gmail.com",std_Dept="English")
    # student_data.save(force_insert=True)
    
    # Student_data, created=Student.objects.get_or_create(std_name='sumona',std_Roll=88,std_Email="sumilon@gmail.com",std_Dept="English")
    # print(created)
    
    # student_data=Student.objects.filter(id=3).update(std_Roll=50)
    
    # Student_data=Student.objects.filter(std_name="sumilon").update(std_Roll=101)
    
    # student_data , created =Student.objects.update_or_create(pk=3, std_name="joya",defaults={'std_name':"Joy bain"})
    # student_data, created = Student.objects.update_or_create(pk=5, std_name='Ripa', defaults={'std_name':'Ripa Roy'})
    # print(student_data)
    
    # obj=[
    #     Student(std_name='Sujon',std_Roll=102,std_Email="sujon@gmail.com",std_Dept="BSC in CSE"),
    #     Student(std_name='Maton',std_Roll=103,std_Email="maton@gmail.com",std_Dept="Bangla"),
    #     Student(std_name='Mahide',std_Roll=104,std_Email="Madhie@gmail.com",std_Dept="BA"),
    #     Student(std_name='Rahim',std_Roll=105,std_Email="Rakhim@gmail.com",std_Dept="BSC in CSE")
    # ]
    
    # student_data=Student.objects.bulk_create(obj)
    
    # all_student_data=Student.objects.all()
    
    # for std in all_student_data:
    #     std.std_Dept = "BSC in CSE"    
    # student_data=Student.objects.bulk_update(all_student_data,['std_Dept'])    
    
    # student_data=Student.objects.in_bulk([1,2])
    
    student_data=Student.objects.in_bulk()
    
    # print(student_data[1].std_name)
    print(student_data)
    
    print(student_data)
    print("=========")
    
    return render(request,'Home.html',locals())
