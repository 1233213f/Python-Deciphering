import uiautomator2  as u2
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

d = u2.connect()

print(d(resourceId="com.hl.train:id/quickTakePhoto").get_text())
print(d(text=u"用户名:").info)
