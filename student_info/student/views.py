from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        student=Student()
        name=request.POST.get('name')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        city=request.POST.get('city')
        student.name=name
        student.lname=lname
        student.email=email
        student.city=city
        student.save()
        return HttpResponse("your details are saved succesfully")
    return render(request,'index.html')