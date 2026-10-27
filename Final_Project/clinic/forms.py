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
            'doctor_id',
            'is_urgent',
        ]

class UnifiedLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))