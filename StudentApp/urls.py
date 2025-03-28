from django.contrib import admin
from django.urls import path,include
from StudentApp import views


urlpatterns = [
    path('Student/',views.StudentInterface,name='Student'),
]
