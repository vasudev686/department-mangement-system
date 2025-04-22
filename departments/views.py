from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def department_list(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})





def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
        
    return render(request, 'create_department.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Department
from .forms import DepartmentForm

def edit_department(request, pk):
    department = get_object_or_404(Department, dept_id=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
           
            return redirect('dashboard')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'edit_department.html', {'form': form})


@login_required
def dashboard(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(dept_name__icontains=query, status=True)
    else:
        departments = Department.objects.filter(status=True)
    return render(request, 'dashboard.html', {'departments': departments})

@login_required
def delete_department(request, pk):
    department = get_object_or_404(Department, dept_id=pk)
    if request.method == 'POST':
        department.status = False
        department.save()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'department': department})

