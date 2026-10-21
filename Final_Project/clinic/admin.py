from django.contrib import admin
from .models import Receptionist, Patient, Doctor, Appointment

# Register your models here.
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)