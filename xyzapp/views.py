from django.shortcuts import render,redirect
from django.http import HttpResponse
from xyzapp.models import Sales
from xyzapp.forms import RegistrationForm
from xyzapp.models import Registration

# Create your views here.
def homepage(request):
    return render(request,'admin/index.html')

def view_sales(request):
    sales_list = Sales.objects.all()
    return render(request,'admin/view_salesdata.html',{'sales_list':sales_list})

def chartpage(request):
    return render(request,'admin/charts.html')    

def registrationpage(request):
    return render(request,'admin/registration.html')

def add_registration_function(request):
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                return redirect('/view_registration')
            except:
                pass
    return render(request,'admin/registration.html',{'form':form})  

def view_registration(request):
    registration_list = Registration.objects.all()
    return render(request,'admin/view_registration.html',{'registration_list':registration_list})