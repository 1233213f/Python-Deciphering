import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
# ͼ�ν���
class unlockTest(unittest.TestCase):
    def test_unlock(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['app'] = '/Users/a140/Downloads/test.apk'
        desired_caps['deviceName'] = '03083025d0250909'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # ����Դ��������
        self.driver.press_keycode(26)
        self.driver.implicitly_wait(2)
        # ����Դ��������
        self.driver.press_keycode(26)
        # ���ý����ķ���
        self.login_unlock()

    # ����
    def login_unlock(self):
        # ͨ��ID�ҵ��Ź����View
        lock_pattern = self.driver.find_element_by_id("com.android.keyguard:id/lockPatternView")
        # ��ȡView��x,y����ֵ
        x = lock_pattern.location.get('x')
        y = lock_pattern.location.get('y')
        # ��ȡView�Ŀ�Ⱥ͸߶�
        width = lock_pattern.size.get('width')
        height = lock_pattern.size.get('height')
        # ƫ����
        offset = width / 6
        # ����Ź����ھŸ����x,y����ֵ
        p11 = int(x + width / 6), int(y + height / 6)
        p12 = int(x + width / 2), int(y + height / 6)
        p13 = int(x + width - offset), int(y + height / 6)
        p21 = int(x + width / 6), int(y + height / 2)
        p22 = int(x + width / 2), int(y + height / 2)
        p23 = int(x + width - offset), int(y + height / 2)
        p31 = int(x + width / 6), int(y + height - offset)
        p32 = int(x + width / 2), int(y + height - offset)
        p33 = int(x + width - offset), int(y + height - offset)
        # �����ƶ�����һ�����ƫ����
        p3 = p13[0] - p11[0]
        sleep(3)
        # ִ���ƶ�����
        TouchAction(self.driver).press(x=p11[0], y=p11[1]).move_to(x=p3, y=0).wait(1000).move_to(x=0, y=p3).wait(
            1000).release().perform()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(unlockTest)
    unittest.TextTestRunner(verbosity=2).run(suite)