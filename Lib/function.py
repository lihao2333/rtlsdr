from django.shortcuts import render
from MapModel.models import Receiver
from django.conf import settings
import zipfile, os
from . import rtl_cloud
def map(request):
    ctx = {}
    ctx['locs'] = Receiver.objects.all()
    x, y, fc, fs, t, agc = getinput(request)
    if x != '' and y != '':
        x = float(x)
        y = float(y)
        ip = Receiver.objects.filter(x=x, y=y)[0].ip
        ctx['output'] = "loc:%s,%s fc:%s MHz fs:%s Hz T:%s s AGC:%s db IP:%s" % (x, y, fc, fs, t, agc, ip)
        genstatic()
    else:
        ctx['output'] = ""
    return render(request, 'map.html', ctx)
def getinput(request):
    x = request.GET.get('x', '')
    y = request.GET.get('y', '')
    fc = request.GET.get('fc', '')
    fs = request.GET.get('fs', '')
    t = request.GET.get('t', '')
    agc = request.GET.get('agc', '')
    return [x, y, fc, fs, t, agc]
def genstatic():
    datas = rtl_cloud.getdata()
    DATA_DIR = settings.BASE_DIR + "/static/data/"
    with open(DATA_DIR + 'data.txt','w') as mfile:
        for data in datas:
            mfile.write(str(data)[1:-2] + '\n')
    azip = zipfile.ZipFile(DATA_DIR + 'data.zip', 'w',zipfile.ZIP_DEFLATED)
    azip.write(DATA_DIR + 'data.txt', 'data.txt')
    azip.close()
