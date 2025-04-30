from django.shortcuts import render
import requests

from .import models as m


# Create your views here.

def index(request):
    # student={
    #     "sname" : "mahesh",
    #     "course" : "python",
    #     "fees" : "20000"
    # }
    # return render(request,"index.html",{"student":student})
    plist=m.product.objects.all()
    return render(request, 'index.html',{'plist':plist})

def Contact(request):
    loginform={
        "username" : "mahesh",
        "password" : "ma@123",
        "Firstname" : "mass",
        "lastname" : "mahesh",
        "email" : "ma@gmail.com",
        "mobile" : "123456789"
    }    
    return render(request,'Contact.html',{"loginform":loginform})

def Gallary(request):
    users={
        'title' : 'hello, Students!',
        'user_authantication' : True,
        'username' : 'Nipuna Tech',
        'courses' : ['python','java','dotnet','angular']
    }
    return render(request,'Gallary.html',users)


def Services(request):
    data=requests.get('https://jsonplaceholder.typicode.com/posts')
    return render(request,'Services.html',{'data':data.json()})