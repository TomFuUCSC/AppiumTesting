from appium.webdriver.common.appiumby import AppiumBy


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class HomeScreen(Base):
    def select_option(self, label):
        nav = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, label)
        
        assert nav.is_displayed()
        assert nav.is_enabled()
        nav.click()
        
        self.driver.back()
