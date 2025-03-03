from django.shortcuts import render, redirect
from  medapp.models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def department(request):
    return render(request,'departments.html')

def doctor(request):
    return render(request,'doctors.html')

def contact(request):
    if request.method == "POST":
        contactme=Contact(
          name = request.POST['name'],
          email = request.POST['email'],
          subject = request.POST['subject'],
          message = request.POST['message'],
        )
        contactme.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')




def appoint(request):
    if request.method == 'POST':
        myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointments.save()
        return redirect('/appoint')

    else:
        return render(request,'appointment.html')
