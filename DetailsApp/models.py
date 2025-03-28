from django.db import models
from django.utils import timezone


# Create your models here.
class Department(models.Model):
  BranchName= models.CharField(max_length=255)

  def __str__(self) :
          return self.BranchName

class Subject(models.Model):
  SubjectName= models.CharField(max_length=255)

  def __str__(self) :
          return self.SubjectName

class Class(models.Model):
  Class= models.CharField(max_length=255)

  def __str__(self) :
          return self.Class

class Semester(models.Model):
  Semester= models.CharField(max_length=255)

  def __str__(self) :
          return self.Semester

class Date_Time(models.Model):
  created_at = models.DateTimeField(default=timezone.now)

# def __str__(self) :
#         return self.Semester


class StudentDatabase(models.Model):
     NAME=models.CharField(max_length=255,null=True )
     CLASS=models.CharField(max_length=255,null=True)
     SUB=models.CharField(max_length=255,null=True)
     
     SEM=models.CharField(max_length=255,null=True)
     USN=models.CharField(max_length=255,null=True)
     ATT=models.BooleanField(default=False,null=True)
     created_at=models.DateField( default=timezone.now())

     def __str__(self):
        return f"{self.NAME} - {self.created_at}- {'Present' if self.ATT else 'Absent'}"