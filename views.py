#from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def maha(request):
  if request.method == 'POST':
    a1=request.POST.get("name")
    a2=request.POST.get("address")
    a3=request.POST.get("empID")
    a4=request.POST.get("staffid")
    a = t1(name=a1,address=a2,empID=a3,staffid=a4)
    a.save()
    print(a1)
    print(a2)
    print(a3)
    print(a4)
  else:
        return render(request,"page2.html",context={})
  return HttpResponse("printed on console please check:")


