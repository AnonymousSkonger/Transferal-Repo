from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PatientForm, DoctorForm, AppointmentForm

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class AppointmentCreateView(TemplateView):
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        context = {
            'patient_form': PatientForm(),
            'doctor_form': DoctorForm(),
            'appointment_form': AppointmentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        patient_form = PatientForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        appointment_form = AppointmentForm(request.POST)

        # Validate and save if valid
        if patient_form.is_valid() and appointment_form.is_valid():
            patient = patient_form.save()
            
            # If a new doctor was filled out or selected via appointment form
            appointment = appointment_form.save(commit=False)
            appointment.patient_id = patient
            appointment.save()
            
            return redirect('home')

        context = {
            'patient_form': patient_form,
            'doctor_form': doctor_form,
            'appointment_form': appointment_form,
        }
        return render(request, self.template_name, context)