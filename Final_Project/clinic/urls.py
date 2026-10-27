from django.urls import path
from .views import (HomePageView, 
                    AboutPageView, 
                    ContactPageView, 
                    AppointmentCreateView, 
                    UnifiedLoginView, 
                    LogoutView, 
                    DashboardRedirectView, 
                    ReceptionistDashboardView, 
                    DoctorDashboardView, 
                    PatientDashboardView)

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('login/', UnifiedLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/redirect/', DashboardRedirectView.as_view(), name="dashboard_redirect"),
    path('dashboard/', ReceptionistDashboardView.as_view(), name="dashboard"),
    path('doctor/dashboard/', DoctorDashboardView.as_view(), name="doctor_dashboard"),
    path('patient/dashboard/', PatientDashboardView.as_view(), name="patient_dashboard"),
    path('book/', AppointmentCreateView.as_view(), name="booking"),
]
