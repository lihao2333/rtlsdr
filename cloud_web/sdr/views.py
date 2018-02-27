from django.shortcuts import render
from .models import Sdr
# Create your views here.
def sdr_list(request):
    sdrs = Sdr.objects.all()
    return render(request,"sdr/list.html", {"sdrs":sdrs} )
def sdr_detail(request, sdr_id):
    sdr = Sdr.objects.get(id=sdr_id)
    return render(request,"sdr/detail.html", {"sdr":sdr} )
