from django.contrib import admin
from .models import StudentModel

# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'rollno', 'school','address']

admin.site.register(StudentModel, StudentModelAdmin)

