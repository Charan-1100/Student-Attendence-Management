from django.contrib import admin
from DetailsApp.models import Department,Subject,Semester,StudentDatabase,Class,Date_Time

# Register your models here.






class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('BranchName',)  # Fields to display in the list view

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('SubjectName',)  # Fields to display in the list view

class SemAdmin(admin.ModelAdmin):
    list_display = ('Semester',)  # Fields to display in the list view
   
class ClassAdmin(admin.ModelAdmin):
    list_display = ('Class',)  # Fields to display in the list view\
    
class StudentDataBaseAdmin(admin.ModelAdmin):
    list_display = ('NAME','USN','SUB','CLASS','created_at','ATT')
    list_filter = ('ATT','SUB')  # Fields to display in the list view    

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Subject,SubjectAdmin)

admin.site.register(Semester,SemAdmin)

admin.site.register(StudentDatabase,StudentDataBaseAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Date_Time)