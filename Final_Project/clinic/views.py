from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Receptionist, Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, UnifiedLoginForm, PatientForm, AppointmentForm

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
    

class UnifiedLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if 'user_type' in request.session:
            return redirect('dashboard_redirect')
        return render(request, self.template_name, {'form': UnifiedLoginForm()})

    def post(self, request):
        form = UnifiedLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # 1. Check if Receptionist
            try:
                rec = Receptionist.objects.get(email=email, password=password, isActive=True)
                request.session['user_type'] = 'receptionist'
                request.session['user_id'] = rec.receptionist_id
                request.session['user_name'] = f"{rec.name} {rec.surname}"
                return redirect('dashboard')
            except Receptionist.DoesNotExist:
                pass

            # 2. Check if Doctor
            try:
                doc = Doctor.objects.get(email=email, password=password, isActive=True)
                request.session['user_type'] = 'doctor'
                request.session['user_id'] = doc.doctor_id
                request.session['user_name'] = f"Dr. {doc.name} {doc.surname}"
                return redirect('doctor_dashboard')
            except Doctor.DoesNotExist:
                pass

            # 3. Check if Patient
            try:
                pat = Patient.objects.get(email=email, password=password, isActive=True)
                request.session['user_type'] = 'patient'
                request.session['user_id'] = pat.patient_id
                request.session['user_name'] = f"{pat.name} {pat.surname}"
                return redirect('patient_dashboard')
            except Patient.DoesNotExist:
                pass

            form.add_error(None, 'Invalid email, password, or inactive account.')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('home')

class DashboardRedirectView(View):
    def get(self, request):
        utype = request.session.get('user_type')
        if utype == 'receptionist':
            return redirect('dashboard')
        elif utype == 'doctor':
            return redirect('doctor_dashboard')
        elif utype == 'patient':
            return redirect('patient_dashboard')
        return redirect('login')

# Receptionist Dashboard (Full Access: Urgency flags, appointments, patient/doctor details)
class ReceptionistDashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('user_type') != 'receptionist':
            return redirect('login')
        
        context = {
            'user_name': request.session.get('user_name'),
            'patients': Patient.objects.all(),
            'doctors': Doctor.objects.all(),
            'appointments': Appointment.objects.all().order_by('-is_urgent', 'appointment_date'),
        }
        return render(request, self.template_name, context)

# Doctor Dashboard (View expected patients, ailment, urgent status)
class DoctorDashboardView(TemplateView):
    template_name = 'doctor_dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('user_type') != 'doctor':
            return redirect('login')
        
        doc_id = request.session.get('user_id')
        doctor = Doctor.objects.get(pk=doc_id)
        appointments = Appointment.objects.filter(doctor_id=doctor).order_by('-is_urgent', 'appointment_date')
        
        context = {
            'user_name': request.session.get('user_name'),
            'doctor': doctor,
            'appointments': appointments,
        }
        return render(request, self.template_name, context)

# Patient Dashboard (View assigned doctor, appointment date, time)
class PatientDashboardView(TemplateView):
    template_name = 'patient_dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('user_type') != 'patient':
            return redirect('login')
        
        pat_id = request.session.get('user_id')
        patient = Patient.objects.get(pk=pat_id)
        appointments = Appointment.objects.filter(patient_id=patient)
        
        context = {
            'user_name': request.session.get('user_name'),
            'patient': patient,
            'appointments': appointments,
        }
        return render(request, self.template_name, context)

class AppointmentCreateView(View):
    template_name = 'booking.html'

    def get(self, request):
        if request.session.get('user_type') != 'receptionist':
            return redirect('login')
        
        context = {
            'patient_form': PatientForm(),
            'appointment_form': AppointmentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.session.get('user_type') != 'receptionist':
            return redirect('login')

        patient_form = PatientForm(request.POST)
        appointment_form = AppointmentForm(request.POST)

        if patient_form.is_valid() and appointment_form.is_valid():
            patient = patient_form.save()
            appointment = appointment_form.save(commit=False)
            appointment.patient_id = patient
            appointment.save()
            return redirect('dashboard')

        context = {
            'patient_form': patient_form,
            'appointment_form': appointment_form,
        }
        return render(request, self.template_name, context)