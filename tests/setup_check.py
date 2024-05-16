import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    platformVersion='13',
    deviceName='Pixel_6_Pro',
    automationName='uiautomator2',
    app='/Users/pablovergara/Desktop/automation/hyacinth/apps/android/ApiDemos-debug.apk',
    language='en',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        time.sleep(2)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
        
    def test_click_media(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Media"]')
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="VideoView"]')
        
        el.click()
        el2.click()


if __name__ == '__main__':
    unittest.main()