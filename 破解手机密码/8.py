import uiautomator2 as u2

d = u2.connect_usb("8681-A01-0xc60fcc9d")
d.app_start(package_name="com.wandoujia.phoenix2")
print("step 1")

d.screen_off()

d.unlock()

points = [
    (0.219, 0.853),
    (0.498, 0.697),
    (0.78, 0.535),
    (0.782, 0.693),
    (0.784, 0.855),
    (0.219, 0.536),
]

d.swipe_points(points=points, duration=0.2)

print("step 2")