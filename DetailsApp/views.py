from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from DetailsApp.models import StudentDatabase,Class,Subject,Semester,Department
from django.contrib.auth import authenticate, login, logout
from StudentApp.models import Students


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def signin(request):
    b=''
    if request.method == 'POST':
        uname = request.POST.get('Uname')
        passwd = request.POST.get('Pwd')
        user = authenticate(request,username=uname,password=passwd)
        if user is not None:
            login(request,user)            
            return redirect('Home')
        else:
            b='Incorrect password or user does not exist'
    return render(request,'login.html',{'b':b})

def signup(request):
    a=''
    b=''
    if request.method == 'POST':
       uname = request.POST.get('Uname')
       uid = request.POST.get('Uid')
       pass1 = request.POST.get('pwd1')
       pass2 = request.POST.get('pwd2')
       if pass1 != pass2:
        a='Password does not matches'
        
       else:

        My_user = User.objects.create_user(uname,uid,pass1)
        My_user.save()
        return redirect("login")
        a ={'uname':n}
    return render(request,'signup.html',{'user':a})


# def Data(request):
#      if request.method =='POST':
#         names = request.POST.getlist('SName')
#         clas = request.POST.get('clas')
#         sub = request.POST.get('sub')
#         sem = request.POST.get('sem')
#         att = request.POST.getlist('att')
#         usn = request.POST.getlist('usn')
#         data=StudentDatabase(NAME=names,SUB=sub,CLASS=clas,SEM=sem,ATT=att,USN=usn)
#         data.save()
#         D='Data Saved Scuessfully'
#      else:
#         P='Please Fill The Form'
   
#      return HttpResponse("Saved Sucessfull")

def Save_Data(request):
    sub = request.POST.get('sub')
    
    
    if request.method == 'POST':
         sem = request.POST.get('sem')
         cls = request.POST.get('CLASS')
         students = Students.objects.filter(Class__Class__icontains=cls,Sem__Semester__icontains=sem)
         
        #  clas = request.POST.get('cls')
         for student in students:
            present = request.POST.get(f'present_{student.id}') == 'on'
            usn = student.USN
            # clas = student.Class
            StudentDatabase.objects.create(NAME=student,USN=usn,ATT=present,SUB=sub,CLASS=cls,SEM=sem)
         return redirect('Home') 
        #  names = request.POST.getlist('SName')
        #  clas = request.POST.get('clas')
        #  sub = request.POST.get('sub')
        #  sem = request.POST.get('sem')
        #  att = request.POST.getlist('att')
        #  usn = request.POST.getlist('usn')
        #  data=StudentDatabase(NAME=names,SUB=sub,CLASS=clas,SEM=sem,ATT=att,USN=usn)
        #  data.save()
        #  m='Data save sucessfully'
    else:
        students = Students.objects.all()
    return render()

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def StudentReport(request):
    Student = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    
    context = {'Student':Student,'subject':subject,'semester':semester,'clas':clas}
    return render(request,'StudentData.html',context)

def Search(request):
    Student = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    
     
    sub = request.GET['sub']
    cls = request.GET['CLASS']
    sem = request.GET['sem']
    name = request.GET['name']
    usn = request.GET['usn']
    # sub = request.GET('sub')
    # cls = request.GET.get('CLASS')
    # sem = request.GET.get('sem')
    data = StudentDatabase.objects.filter(SUB__icontains=sub,CLASS__icontains=cls,SEM__icontains=sem,NAME__icontains=name,USN__icontains=usn)
    context = {'data':data,'Student':Student,'subject':subject,'semester':semester,'clas':clas}
    return render(request,'StudentData.html',context)

def AddStudent(request):
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    dep= Department.objects.all()
    b=''
    if request.method == 'POST':
        uname = request.POST.get('name')
        usn = request.POST.get('usn')
        sem = request.POST.get('sem')
        dep = request.POST.get('dep')
        clas = request.POST.get('CLASS')
        data = Students.objects.create(StudentName=uname,USN=usn,Sem=sem,Department=dep,Class=clas)
        data.save()
    else:
        b='Please fill the blank place'
        
    context = {'subject':subject,'semester':semester,'clas':clas,'dep':dep,'msg':b}
    
    return render(request,"AddStudent.html",context)

def choicepage(request):
    semester = Semester.objects.all()
    clas = Class.objects.all()
    context = {'semester':semester,'clas':clas}
    return render(request,'choice.html',context)


def choice(request):
    # Student = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    cls = request.GET.get('CLASS')
    sem = request.GET.get('sem')
    data = Students.objects.filter(Class__Class__icontains=cls,Sem__Semester__icontains=sem)
     
   
    context = {'data':data,'clas':clas,'semester':semester,'subject':subject,'cls':cls,'sem':sem}
    return render(request,'attendance.html',context)

def StudentList(request):
    students = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    Dep = Department.objects.all()
    clas = Class.objects.all()
    # if request.method == 'GET':
    #     cls = request.GET.get('CLASS')
    #     sem = request.GET.get('sem')
    #     name = request.GET.get('name')
    #     usn = request.GET.get('usn')
    #     data = Students.objects.filter(StudentName__icontains=name,USN__icontains=usn,Class__Class__icontains=cls,Sem__Semester__icontains=sem)
    #     return redirect('StudentList',{'data':data})
    # else:
    #     data =  students = Students.objects.all()
    context = {'subject':subject,'semester':semester,'clas':clas,'students':students,'Dep':Dep}
    return render(request,'StudentList.html',context)

def SearchList(request):
    students = Students.objects.all()
    subject = Subject.objects.all()
    semester = Semester.objects.all()
    clas = Class.objects.all()
    cls = request.GET.get('CLASS')
    sem = request.GET.get('sem')
    name = request.GET.get('name')
    dep = request.GET.get('dep')
    data = Students.objects.filter(StudentName__icontains=name,Class__Class__icontains=cls,Sem__Semester__icontains=sem,Department__BranchName__icontains=dep)
    context = {'data':data,'subject':subject,'semester':semester,'clas':clas,'students':students}
    return render(request,'Sortedlist.html',context)