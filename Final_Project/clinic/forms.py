from django import forms
from .models import Receptionist, Patient, Doctor, Appointment


class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = [
            'name',
            'surname',
            'id_number',
            'age',
            'email',
            'phoneNumber',
            'password',
            'isActive',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'surname',
            'id_number',
            'age',
            'email',
            'phoneNumber',
            'password',
            'isActive',
            'ailment',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'name',
            'surname',
            'id_number',
            'age',
            'email',
            'phoneNumber',
            'password',
            'isActive',
            'profession',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient_id',
            'doctor_id',
        ]
    class Meta:
            model = Appointment
            fields = [
                'doctor_id',
            ]