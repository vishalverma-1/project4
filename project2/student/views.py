from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pal
def run(request):
    return HttpResponse("i am sleeping")


def verma(request):
    return render(request,'pal.html')


def myfun(request):
    if request.method=='POST':
       name=request.POST.get('name')
       age=request.POST.get('age')
       email=request.POST.get('email')
       mobile=request.POST.get('mobile')
       data=pal.objects.create(name=name,age=age,email=email,mobile=mobile)
       data.save() 
       return redirect('home')
    else:
         return render(request,'verma.html')    
    
def read(request):
    data=pal.objects.all()
    return render(request,'read.html',{'data':data})
        
def delt(request,id):
    data=pal.objects.get(id=id)
    data.delete()
    return redirect ('home')

def edit(request,id):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        mobile=request.POST['mobile']
        i=pal.objects.filter(id=id).update(name=name,age=age,email=email,mobile=mobile)
        return redirect('home')
    else:
        da=pal.objects.filter(id=id)
        return render(request,'edit.html',{'data':da})


     
 

    
