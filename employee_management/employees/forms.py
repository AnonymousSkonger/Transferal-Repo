from django import forms
from .models import Employee, Department, JobPosition, EmployeeRecord

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
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

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'departmentCode',
            'departmentName',
            'description',
            'isActive',
        ]

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = [
            'positionCode',
            'positionName',
            'description',
            'minimumSalary',
            'maximumSalary',
            'isActive',
        ]

    def clean(self):
        cleaned_data = super().clean()
        minimum_salary = cleaned_data.get('minimumSalary')
        maximum_salary = cleaned_data.get('maximumSalary')

        if minimum_salary is not None and maximum_salary is not None:
            if maximum_salary < minimum_salary:
                raise forms.ValidationError(
                    'Maximum salary cannot be lower than the minimum salary.'
                )
        return cleaned_data


class EmployeeRecordForm(forms.ModelForm):
    class Meta:
        model = EmployeeRecord
        fields = [
            'employee',
            'department',
            'jobPosition',
            'comments',
        ]