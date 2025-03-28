from django.contrib import admin
from StudentApp.models import Students
# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentName',)  # Fields to display in the list view
    search_fields = ('StudentName',)          # Add a search box for the name field


admin.site.register(Students,StudentAdmin)