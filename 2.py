if(iface.status()!=const.IFACE_CONNECTED):
  profile = pywifi.Profile()
  profile.ssid = 'vivo X7'
  profile.auth = const.AUTH_ALG_OPEN     #需要秘密
  profile.akm.append(const.AKM_TYPE_WPA2PSK) #加密类型
  profile.cipher = const.CIPHER_TYPE_CCMP   #加密单元
  #profile.key = '123456789'         #在此输入你的wifi密码
  profile.key = password
  #time.sleep(3)
  wifi = pywifi.PyWiFi()
  iface = wifi.interfaces()[0] # 取一个无限网卡
  profile = iface.add_network_profile(profile)
  iface.connect(profile)
  time.sleep(3)    #程序休眠时间3秒；如果没有此句，则会打印连接失败，因为它需要一定的检测时间
  if iface.status()==const.IFACE_CONNECTED:
    print("连接成功！！！")
  else:
    print("连接失败！！！")
    isok=False
  return isok
else:
  print("已经连接网络")
  return isok