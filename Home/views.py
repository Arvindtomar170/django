from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        if password=='123':
             return render(request,'home.html')
    return render(request,'login.html')

    
def servises(request):
             return render(request,'servises.html')
    
def about(request):
      return render(request,'about.html')

def contact(request):
      msg={'a':6}
      if request.method=="POST":
            first_nam=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            # obj=Contact(first_name=first_nam,last_name=last_name,phone=phone,email=email,date=datetime.today())
            obj=Contact(first_name=first_nam,last_name=last_name,phone=phone,email=email,date=datetime.today(), extra="this is extra coulumn")
            obj.save()
            messages.success(request,"your message has been send")
      return render(request,'contact.html')

def index(request):
      return render(request,'index.html')