import pywifi
from pywifi import *
import time
def CrackWifi(password):
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0] # 取一个无限网卡
# 是否成功的标志
isok = True