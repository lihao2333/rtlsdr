
from rtlsdr import RtlSdrTcpClient
def getdata():
    client = RtlSdrTcpClient(hostname='10.112.216.60', port=12345)
    client.center_freq = 2e6
    data = client.read_samples()
    return data
