from django import forms
from .models import Receptionist, Patient, Doctor, Appointment


class RecpetionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = [
            'name',
            'surname',
            'id_number',
            'email',
            'phoneNumber',
            'age',
            'salary',
            'dateHired',
            'isActive',
        ]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'surname',
            'id_number',
            'email',
            'phoneNumber',
            'age',
            'salary',
            'dateHired',
            'isActive',
            'ailment',
        ]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'name',
            'surname',
            'id_number',
            'email',
            'phoneNumber',
            'age',
            'salary',
            'dateHired',
            'profession',
            'isActive',
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
            model = Appointment
            fields = [
                'patient_id',
                'doctor_id',
                'appointment_entered',
            ]