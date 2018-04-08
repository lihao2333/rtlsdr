import time
from rtlsdr import RtlSdrTcpClient
def getdata():
   # client = RtlSdrTcpClient(hostname='10.112.216.60', port=12345)
    client = RtlSdrTcpClient(hostname='10.42.0.69', port=2333)
    client.center_freq = 2e6
    data = client.read_samples()
    client.mytime=time.time()+3
    print(len(data))
    return data
getdata()
