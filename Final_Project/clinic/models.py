from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Receptionist(models.Model):
    receptionist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    id_number = models.CharField(
            unique=True,
            null=False,
            max_length=13,
            blank=False,
            validators=[
                RegexValidator(
                    regex=r'^\d{13}$',
                    message='ID number must consist of exactly 13 digits.'
                )
            ],
        )
    age = models.PositiveIntegerField(null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phoneNumber = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r'^\+?\d{9,15}$',
                    message='Enter a valid phone number (9 to 15 digits, optional leading +).'
                )
            ]
        )
    password = models.CharField(max_length=128, null=False, blank=False)
    isActive = models.BooleanField(default=True)
    dateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    id_number = models.CharField(
        unique=True,
        null=False,
        max_length=13,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='ID number must consist of exactly 13 digits.'
            )
        ],
    )
    age = models.PositiveIntegerField(null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phoneNumber = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r'^\+?\d{9,15}$',
                    message='Enter a valid phone number (9 to 15 digits, optional leading +).'
                )
            ]
        )
    password = models.CharField(max_length=128, null=False, blank=False)
    isActive = models.BooleanField(default=True)
    dateRegistered = models.DateTimeField(auto_now_add=True)
    ailment = models.TextField(blank=False)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    id_number = models.CharField(
            unique=True,
            null=False,
            max_length=13,
            blank=False,
            validators=[
                RegexValidator(
                    regex=r'^\d{13}$',
                    message='ID number must consist of exactly 13 digits.'
                )
            ],
        )
    age = models.PositiveIntegerField(null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phoneNumber = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r'^\+?\d{9,15}$',
                    message='Enter a valid phone number (9 to 15 digits, optional leading +).'
                )
            ]
        )
    password = models.CharField(max_length=128, null=False, blank=False)
    isActive = models.BooleanField(default=True)
    profession = models.CharField(max_length=100)
    dateRegistered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Appointment(models.Model):
    patient_id = models.ForeignKey("Patient", verbose_name=("Appointment"), on_delete=models.CASCADE)
    doctor_id = models.ForeignKey("Doctor", verbose_name=("Appointment"), on_delete=models.CASCADE)
    appointment_entered = models.DateField(auto_now_add=True)
