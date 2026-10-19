from django.contrib import admin
from .models import Employee, Department, JobPosition, EmployeeRecord

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(JobPosition)
admin.site.register(EmployeeRecord)