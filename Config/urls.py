"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from DetailsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Home'),
    path('login/',views.signin,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.log_out,name='signout'),
    path('Faculty/', include('FacultyApp.urls')),
    path('Students/', include('StudentApp.urls')),
    path('data/',views.Save_Data,name='data'),
    path('StudentReport/',views.StudentReport,name='SR'),
    path('search/',views.Search,name='srch'),
    path('AddStudent/',views.AddStudent,name='Add'),
    path('choice/',views.choice,name='choice'),
    path('choicepage/',views.choicepage,name='choicepage'),
    path('StudentList/',views.StudentList,name='StudentList'),
    path('SearchList/',views.SearchList,name='SearchList')
]
