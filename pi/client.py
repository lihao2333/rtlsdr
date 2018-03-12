#!/usr/bin/pyhon 
from rtlsdr import RtlSdrTcpServer
server = RtlSdrTcpServer(hostname='0.0.0.0', port=2333)
server.run_forever()
