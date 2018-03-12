from rtlsdr import RtlSdrTcpClient
import time
client = RtlSdrTcpClient(hostname='10.112.216.60', port=2333)
client.center_freq = 2e6
client.gain = 4
client.mytime= time.time()+3
data = client.read_samples()
print(len(data))
