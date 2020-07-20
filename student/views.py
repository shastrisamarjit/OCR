from django.shortcuts import render,redirect
#from student.forms import Studentform
from student.models import Studenttable
from django.contrib import messages

def studentpage(request):
    return render(request,"student/studentpage.html")
def registerstudent(request):
    return  render(request,"student/registerstudent.html")
def savestudent(request):
    n=request.POST.get("r1")
    cn=request.POST.get("r2")
    e=request.POST.get("r3")
    p=request.POST.get("r4")
    #if sf.is_valid():
    #    sf.save()
    Studenttable(name=n,contactno=cn,email=e,password=p).save()
    messages.success(request,"Registered Successfully")
    return redirect("registerstudent")
    #else:
    #    return render(request,"student/registerstudent.html")
def loginstudent(request):
    return render(request,"student/loginstudent.html")
def checkloginstudent(request):
    x=request.POST.get("l1")
    y=request.POST.get("l2")
    try:
        Studenttable.objects.get(email=x,password=y)
        return render(request,"student/studenthome.html",{"name":x})
    except Studenttable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("checkloginstudent")

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

@method_decorator(csrf_exempt,name='dispatch')
def phoneurl_view(request):
    pnum = request.POST.get('cname')
    try:
        Studenttable.objects.get(contactno=pnum)
        data={'error':'Contact number taken'}
    except Studenttable.DoesNotExist:
        data={'message':'Contact number available'}
    return JsonResponse(data)

