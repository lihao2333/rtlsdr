from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.conf import settings
from rtlsdr import RtlSdrTcpClient
from .forms import DataUploadForm
from sdrpub.models import Sdr
import time as ttime
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
def data_get(request):
    if "sdr_ip" in request.GET:
        sdr_ip = request.GET['sdr_ip']
        #user= User.objects.get(username="geek")
        user = request.user
        sdr = Sdr.objects.get(ip=sdr_ip)
        loc_x = sdr.loc_x
        loc_y = sdr.loc_y
        fs = request.GET['fs']
        dt = request.GET['dt']
        fc = request.GET['fc']
        gain = request.GET['agc']
        client = RtlSdrTcpClient(hostname=sdr_ip, port=2333)
        client.center_freq = float(fc)
        client.sample_rate = float(fs)
        client.gain = float(gain)
        client.mytime = ttime.time()+3
        datas = client.read_samples(float(dt)*float(fs))
        time = timezone.now()
        data_path="user_{0}/{1}.txt".format(user.username, time)
        with open(settings.MEDIA_ROOT+data_path,"w") as data_file:
            data_file.write("fs={0},dt={1},fc={2},gain={3},loc_x={4},loc_y={5},owner={6}\n".format(fs,dt,fc,gain,loc_x,loc_y,user.username))
            for data in datas:
                data_file.write(str(data)+'\n')
        data = Data(owner=user, loc_x=loc_x ,loc_y=loc_y, fs=fs, fc=fc, dt=dt, data=data_path,gain=gain,time=time)
        data.save()
        return HttpResponse("data get successful\n"+str(len(datas)))
    else:
        sdrs = Sdr.objects.all()
        print(sdrs)
        return render(request, "data/get.html", {"sdrs":sdrs})
