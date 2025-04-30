# Django app creation 

# step 1: python manage.py startapp shoppy

# step 2: create urls.py in shoppy

# step 3: myapp->views.py 

# ------------------------------
# from django,shortcuts import render

# def index(request):
#     return render(request,"index.html")

from django.urls import path 
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('Contact',views.Contact,name='Contact'),
    path('Gallary',views.Gallary,name='Gallary'),
    path('Services',views.Services,name='Services')
]

