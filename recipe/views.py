from django.shortcuts import render, HttpResponse , redirect

from .models import *

# Create your views here.
def home(request):

    employees = Employees.objects.all()

    context = {
        'employees' :employees,
    }


    return render(request,"home.html",context=context)

def add(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name = name,
            email = email,
            address = address,
            Mobile = phone,
        )
        emp.save()

        return redirect('homepage')

    return render(request,"home.html")
def edite(request):
    employees = Employees.objects.all()

    context = {
        'employees' :employees,
    }


    return render(request,"home.html",context=context)

def update(request,id):

    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        empl = Employees(
            id = id ,
            name = name,
            email = email,
            address = address,
            Mobile = phone,
        )
        empl.save()

        return redirect('homepage')

    return render(request,"home.html")

def delete(request,id):

    employees = Employees.objects.filter(id=id)
    employees.delete()

    context = {
        'employees' :employees,
    }


    return redirect('homepage')
   


    


