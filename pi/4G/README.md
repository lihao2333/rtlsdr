## 上网卡
[购买链接]( https://detail.tmall.com/item.htm?id=538368357894&skuId=3215576226356 )  
[参考教程](http://blog.csdn.net/u012731379/article/details/78732774/)
其他教程
* http://blog.csdn.net/jiaojian8063868/article/details/79295570
* http://blog.csdn.net/qq_32384313/article/details/77725235
* [树莓派+华为HUAWEI ME909s-821](http://blog.csdn.net/qq_32384313/article/details/77725235)
* http://blog.csdn.net/jiaojian8063868/article/details/79295570


问题
* TargetVendor/Product?
* usb_modeswitch.d/file content
  * `Init2 = ATQ V1 E1 S0=0 &C1 &D2 +FCLASS=0`  Bad init str
  * `Init5 = AT+CGDCONT=1, "IP", "3GNET"` Bad Init str
  * `AT&F &D2 &C1` Bad Init str
  * invalid idal command
    * https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=67337
    * https://ubuntuforums.org/showthread.php?t=879683
    * https://www.raspberrypi.org/forums/viewtopic.php?t=109591
    * https://ubuntuforums.org/archive/index.php/t-1527511.html
  * APN
    * http://franson.com/forum/topic.asp?TOPIC_ID=6669
    * http://samiux.wordpress.com/2008/04/...on-ubuntu-804/
    * https://forge.betavine.net/frs/downl...99.17_i386.deb
    * http://blog.csdn.net/qq_32384313/article/details/77725235
  * Network manager  
* no wifi
* AT 指令
  * https://wenku.baidu.com/view/84bbe5430c22590103029d3e.html

收获
* `sudo minicom -D /dev/ttyUSB0` 发送at指令
* `AT+CFUN=0 `
* 可用at
  * at+cpin?
  * at+cpin=1234
  * at+cfun=0
  * http://blog.csdn.net/u011784994/article/details/54603549
## 解决啦！！！
* 之前指令不成功是因为没有输入pin, 为了方便起见，在一台windows上用自带软件把pin密码取消
* 通过wvdialconf可以看到我的板子最多波特率是9600 所以要把教程中的15200改为9600

