from django.shortcuts import render,redirect
from app.forms import Adminform,Scheduleform
from app.models import Admintable,Scheduletable
from django.contrib import messages
from django.db.utils import IntegrityError

def adminlogin(request):
    return render(request,"app/adminlogin.html",{"admin":Adminform})

def adminsave(request):
    x=request.POST.get("name")
    y=request.POST.get("pas")
    try:
        Admintable.objects.get(name=x,pas=y)
        return render(request,"app/adminpage.html")
    except  Admintable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("adminsave")
def schedule(request):
    return render(request,'app/schedulepage.html',{"schedule":Scheduleform})
def schedulesave(request):
    #n=request.POST.get("name")
    #f=request.POST.get("faculty")
    #d=request.POST.get("date")
    #fe=request.POST.get("fee")
    #du=request.POST.get("duration")
    #print("name")
    #print(f)
    #print(d)
    #print(fe)
    #print(du)
    #print(sf)
    sf=Scheduleform(request.POST)
    if sf.is_valid():
        sf.save()
        #Scheduletable(name=n,faculty=f,date=d,fee=fe,duration=du).save()
        messages.success(request,"Registered Successfully")
        return redirect("schedule")
    else:
        messages.error(request,"wrong input")
        return render(request,"app/schedulepage.html",{"schedule":sf})
def viewschedule(request):
    schedule_data=Scheduletable.objects.all()
    return render(request,"app/viewschedule.html",{"data":schedule_data})
def deleteschedule(request):
    x=request.GET.get("no")
    Scheduletable.objects.filter(name=x).delete()
    y=Scheduletable.objects.all()
    return render(request,"app/viewschedule.html",{"data":y})
#def updateschedule(request):
#    x=request.GET.get("no")
#    y=Scheduletable.objects.get(name=x)
#   return render(request,"app/")