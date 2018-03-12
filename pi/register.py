import urllib
import urllib2

url = "http://10.42.0.1:8000/sdrpub/register?name=sdr_02&loc_x=7500&loc_y=200"

req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
