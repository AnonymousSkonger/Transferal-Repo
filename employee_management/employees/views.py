from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Employee, Department, JobPosition, EmployeeRecord
from .forms import EmployeeForm, DepartmentForm, JobPositionForm, EmployeeRecordForm

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(
        request,
        'employees/employee_detail.html',
        {'employee': employee}
    )

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(
        request,
        'employees/employee_confirm_delete.html',
        {'employee': employee}
    )