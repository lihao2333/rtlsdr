#!/usr/bin/python
#-*- coding:utf8 -*-
from rtlsdr import RtlSdrTcpClient
from matplotlib.pyplot import psd,xlabel,ylabel,show
import cgi, cgitb 
def getInput():
	form = cgi.FieldStorage() 
	hostname = form.getvalue('hostname')
	return hostname
	
def getSamples(hostname):
	client = RtlSdrTcpClient(hostname=hostname, port=12345)
	client.center_freq = 95e6
	client.sample_rate=2.4e6
	client.gain=4
	samples = client.read_samples(256*1024)
	return samples
	print len(samples)
def plotPSD(samples):
	psd(samples, NFFT=1024, Fs=2.4, Fc=95)
	xlabel('Frequency (MHz)')
	ylabel('Relative power (dB)')
	savefig("%s.jpg",hostname)
def display(hostname):
	print "Content-type:text/html"
	print                               # 空行，告诉服务器结束头部
	print '<html>'
	print '<head>'
	print '<meta charset="utf-8">'
	print '<title>Hello %s - 我的第一个 CGI 程序！</title>'%(hostname)
	print '</head>'
	print '<body>'
	print '<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>'
	print '</body>'
#hostname = getInput()
display("asdf")
#samples = getSamples(hostname)
#plotPSD(samples)
