from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import DataUploadForm
# Create your views here.
def data_list(request):
    datas = Data.objects.filter(owner=request.user)
    return render(request, "data/list.html", {"datas":datas})
def data_detail(request, data_id):
    data = Data.objects.get(id=data_id,owner=request.user)
    return render(request, "data/detail.html", {"data":data})

@csrf_exempt
def data_upload(request):
    if request.method == "POST":
        user= User.objects.get(username="geek")
        loc_x =request.POST['loc_x']
        loc_y =request.POST['loc_y']
        fs =request.POST['fs']
        dt =request.POST['dt']
        fc =request.POST['fc']
        agc =request.POST['agc']
        psd =request.FILES['psd']
        data =request.FILES['data']
        time =request.POST['time']
        m_data = Data(owner=user,loc_x=loc_x, loc_y=loc_y, fs=fs, dt=dt, fc=fc, agc=agc, psd=psd, data=data)
        m_data.save()
        print("ok")
#       form = DataUploadForm(request.POST, request.FILES)
#       if form.is_valid():
#           print("ok")
#           form.save()
#       else:
#           print("error")
        return HttpResponse("success")
    else:
        return HttpResponse("fail")