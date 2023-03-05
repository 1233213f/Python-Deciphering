from appium import webdriver
from time import sleep
desired_caps={
   'platformName':'Android',
   'platformVersion':'6.0.1',
   'deviceName':'127.0.0.1:21305',
   'appPackage':'com.baidu.homework',
   'appActivity':'com.baidu.homework.activity.index.IndexActivity',
    'automationName':'Appium',
    'noReset':False
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#获取屏幕size
size = driver.get_window_size()
print(size)
#屏幕的宽度 width
x=size['width']
#屏幕的高度 height
y=size['height']

def swipe_left():
    """
    向左滑动
    """
    x1=x*0.9
    y1=y*0.5
    x2=x*0.1
    t=1000
    n=1#n表示滑动次数
    sleep(1)
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)


from appium import webdriver
from time import sleep
desired_caps={
   'platformName':'Android',
   'platformVersion':'6.0.1',
   'deviceName':'127.0.0.1:21305',
   'appPackage':'com.baidu.homework',
   'appActivity':'com.baidu.homework.activity.index.IndexActivity',
    'automationName':'Appium',
    'noReset':False
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#获取屏幕size
size = driver.get_window_size()
print(size)
#屏幕的宽度 width
x=size['width']
#屏幕的高度 height
y=size['height']

def swipe_right():
    """
    向右滑动
    """
    x1=x*0.1
    y1=y*0.5
    x2=x*0.9
    t=1000
    n=2#n表示滑动次数
    sleep(1)
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)


from appium import webdriver
from time import sleep
desired_caps={
   'platformName':'Android',
   'platformVersion':'6.0.1',
   'deviceName':'127.0.0.1:21305',
   'appPackage':'com.baidu.homework',
   'appActivity':'com.baidu.homework.activity.index.IndexActivity',
    'automationName':'Appium',
    'noReset':False
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#获取屏幕size
size = driver.get_window_size()
print(size)
#屏幕的宽度 width
x=size['width']
#屏幕的高度 height
y=size['height']

def swipe_down():
    """
    向下滑动
    """
    x1=x*0.5
    y1=y*0.1
    y2=y*0.9
    t=1000
    n=3#n表示滑动次数
    sleep(1)
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)


from appium import webdriver
from time import sleep
desired_caps={
   'platformName':'Android',
   'platformVersion':'6.0.1',
   'deviceName':'127.0.0.1:21305',
   'appPackage':'com.baidu.homework',
   'appActivity':'com.baidu.homework.activity.index.IndexActivity',
    'automationName':'Appium',
    'noReset':False
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#获取屏幕size
size = driver.get_window_size()
print(size)
#屏幕的宽度 width
x=size['width']
#屏幕的高度 height
y=size['height']

def swipe_up():
    """
    向上滑动
    """
    x1=x*0.5
    y1=y*0.9
    y2=x*0.1
    t=10000
    n=2#n表示滑动次数
    sleep(1)
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)