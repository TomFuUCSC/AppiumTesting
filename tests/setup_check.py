import unittest
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

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
        
    def test_navigate_to_audioFX(self) -> None:
        media_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Media"]')
        audio_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="AudioFx"]')
    
        media_button.click()
        
        self.assertIsNotNone(audio_button) 
        audio_button.click()
    
    def test_navigate_to_mediaPlayer(self) -> None:
        media_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Media"]')
        media_player = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="MediaPlayer"]')
    
        media_button.click()
        
        self.assertIsNotNone(media_player) 
        media_player.click()
    
    def test_navigate_to_video_view(self) -> None:
        media_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Media"]')
        video_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="VideoView"]')
        video_player = self.driver.find_element(by=AppiumBy.ID, value='io.appium.android.apis:id/surface_view')

        self.assertIsNotNone(media_button)        
        media_button.click()
        video_button.click()
        self.assertIsNotNone(video_player)
        

if __name__ == '__main__':
    unittest.main()