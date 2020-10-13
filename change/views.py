from django.shortcuts import render,redirect
from .models import Change_picture

def change_home(request):

    data=Change_picture.objects.all()

    return render(request,'change/change_page.html',{'data':data})
