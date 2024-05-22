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
        
    def alert_is_visible(self, alert):
        popup = self.driver.find_element(AppiumBy.XPATH, f"{alert}")
        assert popup.is_displayed()
        
    def confirm_alert_title(self, alert_title):
        text = self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name=f"{alert_title}"]')
        assert text.is_displayed()
        
    def alert_action(self, action):
        button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{action}")
        assert button.is_displayed()
        assert button.is_enabled()
        button.click()
        
    def sheet_action(self, action):
        button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{action}")
        assert button.is_displayed()
        assert button.is_enabled()
        button.click()
        
    def enter_text(self, text_input, text_value):
        input = self.driver.find_element(AppiumBy.XPATH, f"{text_input}")
        assert input.is_displayed()
        input.click()
        input.send_keys(text_value)