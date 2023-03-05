import uiautomator2 as u2

d = u2.connect_usb("8681-A01-0xc60fcc9d")

d.screen_off()  # 息屏
d.screen_on()  # 仅仅是点亮平面
d.unlock()  # 进入解锁界面
d.info.get("screenOn")  # 获取当前屏幕状态，如果是亮就为True，息屏就为False
d.press("home")  # 按下home键
d.press("back")  # 按下back键
d.swipe_ext("right")  # 右滑动
d.swipe_ext("left")  # 左移动
d.swipe_points([], duration)  # 滑动到指定list点，duration为延时单位为s