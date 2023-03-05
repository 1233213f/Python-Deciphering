#CrackWifi()
def PasswordFile():
pathfile=“H:/wififile.txt” #你的密码字典
files=open(pathfile,‘r')
while True:
fp=files.readline()
if not fp:
break