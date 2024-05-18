from appium.webdriver.common.appiumby import AppiumBy
import time


class Base(object):
    def __init__(self, driver):
        self.driver = driver
       
        
class AppAction(Base):
    def click_button(self, label):
        nav = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{label}")

        assert nav.is_displayed()
        assert nav.is_enabled()
        nav.click()
        time.sleep(0.5)
