from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Employee(models.Model):
    employeeNumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='ID number must be exactly 13 digits.'
            )
        ]
    )
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message='Enter a valid phone number (9 to 15 digits, optional leading +).'
            )
        ]
    )
    age = models.PositiveIntegerField()
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    dateHired = models.DateField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employeeNumber} - {self.name} {self.surname}"

class Department(models.Model):
    departmentCode = models.CharField(max_length=10, primary_key=True)
    departmentName = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.departmentCode} - {self.departmentName}"

class JobPosition(models.Model):
    positionCode = models.CharField(max_length=10, primary_key=True)
    positionName = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    minimumSalary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    maximumSalary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    isActive = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if (
            self.minimumSalary is not None
            and self.maximumSalary is not None
            and self.minimumSalary > self.maximumSalary
        ):
            raise ValidationError(
                'Minimum salary cannot be greater than maximum salary.'
            )

    def __str__(self):
        return f"{self.positionCode} - {self.positionName}"

class EmployeeRecord(models.Model):
    recordNumber = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='records'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='records'
    )
    jobPosition = models.ForeignKey(
        JobPosition,
        on_delete=models.PROTECT,
        related_name='records'
    )
    dateAssigned = models.DateField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"Record {self.recordNumber}: {self.employee} | "
            f"{self.department.departmentName} | {self.jobPosition.positionName}"
        )