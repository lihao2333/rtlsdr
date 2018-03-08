from django.shortcuts import render
from django.http import HttpResponse
from .models import Sdr
# Create your views here.
def sdr_list(request):
    sdrs = Sdr.objects.all()
    return render(request,"sdr/list.html", {"sdrs":sdrs} )
def sdr_detail(request, sdr_ip):
    sdr = Sdr.objects.get(ip=sdr_ip)
    return render(request,"sdr/detail.html", {"sdr":sdr} )
def sdr_register(request):
    name = request.GET['name']
    loc_x = request.GET['loc_x']
    loc_y = request.GET['loc_y']
    ip = request.META['REMOTE_ADDR']
    sdr =Sdr(name=name, loc_x=loc_x, loc_y=loc_y, ip=ip)
    sdr.save()
    return HttpResponse("register successful"+ip)
