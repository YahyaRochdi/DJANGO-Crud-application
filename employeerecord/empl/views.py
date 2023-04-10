from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.
from .models import Employee
from .forms import EmployeeForm

def randompassword(request):
    random_password =User.objects.make_random_password()
    return render(request,'addEmp.html',{'password':random_password})
    

def plot_employee(request):
    emps=Employee.objects.all
    empDevops = Employee.objects.filter(Departement='DevOps').count()
    empCloud  = Employee.objects.filter(Departement='Cloud').count()
    empHR     =  Employee.objects.filter(Departement='HR').count()
    empReseau =Employee.objects.filter(Departement='Réseau').count()
    empSec    =Employee.objects.filter(Departement='Securité').count()
    empFinance =Employee.objects.filter(Departement='Finance').count()
    empOther   = Employee.objects.filter(Departement='Other').count()
    y = []
    mylabels=[]

    empDict={"DevOps":empDevops,"Cloud":empCloud,"HR":empHR, "Réseau":empReseau,"Securité":empSec,'Finance':empFinance,'Other':empOther}
    for e in empDict :
        if empDict[e] != 0:
            y.append(empDict[e])
            mylabels.append(e)



   # y = np.array([empDevops, empCloud, empHR, empReseau,empSec,empFinance,empOther])
   # mylabels = ["DevOps", "Cloud", "HR", "Réseau","Securité",'Finance','Other']

    plt.pie(y, labels = mylabels)
    plt.show() 
    context = {
        'emps': emps
    }
    return render(request, 'emp/index.html', context)
        
def all_employees(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'emp/index.html', context)


from django.contrib import messages


def add_employees(request):
    
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"Employee {form.cleaned_data.get('name')} has been added")
        return redirect('allEmp')

    context = {
        'form': form,
    }
    return render(request, 'emp/addEmp.html', context)


def edit_employees(request, id=None):
    one_emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=one_emp)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
        return redirect('allEmp')

    context = {
        'form': form,
    }
    return render(request, 'emp/editEmp.html', context)


def one_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    context = {
        'emp': emp
    }
    return render(request, 'emp/viewEmp.html', context)


def delete_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        messages.add_message(request, messages.INFO, f"{emp.name} Employee Deleted")
        return redirect('allEmp')
    context = {
        'emp': emp
    }
    return render(request, 'emp/delete.html', context)


def home_view(request):
    context = dict()
    return render(request, 'emp/home.html', context)
