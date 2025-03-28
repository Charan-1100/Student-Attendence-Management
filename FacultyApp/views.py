from django.shortcuts import render

from StudentApp.models import Students
from DetailsApp.models import Class,Subject,Semester,Date_Time

# Create your views here.

def FacultyInterface(request):

    Student = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    
    context = {'Student':Student,'subject':subject,'semester':semester,'clas':clas}
    return render(request,'faculty interface.html',context)