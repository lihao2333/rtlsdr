from rtlsdr import RtlSdrTcpClient
client = RtlSdrTcpClient(hostname='10.112.216.60', port=2333)
client.center_freq = 2e6
data = client.read_samples()
print(len(data))
