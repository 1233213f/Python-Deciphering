import uiautomator2 as u2

d = u2.connect('192.168.5.4')  # alias for u2.connect_wifi('192.168.5.4')
print(d.info)
d.healthcheck()
d = u2.connect_usb("{Your-Device-Serial}")
d.service("uiautomator").stop()
>>> d.debug = True
>>> d.info
12:32:47.182 $ curl -X POST -d '{"jsonrpc": "2.0", "id": "b80d3a488580be1f3e9cb3e926175310", "method": "deviceInfo", "params": {}}' 'http://127.0.0.1:54179/jsonrpc/0'
12:32:47.225 Response >>>
{"jsonrpc":"2.0","id":"b80d3a488580be1f3e9cb3e926175310","result":{"currentPackageName":"com.android.mms","displayHeight":1920,"displayRotation":0,"displaySizeDpX":360,"displaySizeDpY":640,"displayWidth":1080,"productName"
:"odin","screenOn":true,"sdkInt":25,"naturalOrientation":true}}
<<< EN
d.app_install（' http://some-domain.com/some.apk '）
d.app_start（“ com.example.hello_world ”）＃ start包名称

＃相当于`am force-stop`，因此你可能丢失数据
d.app_stop（ “ com.example.hello_world ”）
＃相当于`pm clear`
d.app_clear（ ' com.example.hello_world '
# push to a folder
d.push("foo.txt", "/sdcard/")
# push and rename
d.push("foo.txt", "/sdcard/bar.txt")
# push fileobj
with open("foo.txt", 'rb') as f:
    d.push(f, "/sdcard/")
# push and change file access mode
d.push("foo.sh", "/data/local/tmp/", mode=0o755)

d.pull("/sdcard/tmp.txt", "tmp.txt")

# FileNotFoundError will raise if the file is not found on the device
d.pull("/sdcard/some-file-not-exists.txt", "tmp.txt")

d.disable_popups（） ＃自动跳过弹出窗口
d.disable_popups（假）＃禁用自动跳过弹出窗口
sess = d.session（“ com.netease.cloudmusic ”）
sess = d.session（“ com.netease.cloudmusic ”，attach = True）

# When app is still running
sess(text="Music").click()  # operation goes normal

# If app crash or quit
sess(text="Music").click()  # raise SessionBrokenError
# other function calls under session will raise SessionBrokenError too

# check if session is ok.
# Warning: function name may change in the future
sess.running() # True or False
