from appium.webdriver.common.appiumby import AppiumBy


class Base(object):
    def __init__(self, driver):
        self.driver = driver
  
        
class MediaScreen(Base):
    def select_audio_fx(self):
        audio_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'AudioFx')
    
        assert audio_button.is_displayed()
        audio_button.click()
    
    def select_media_player(self):
        mediaPlayer_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'MediaPlayer')
    
        assert mediaPlayer_button.is_displayed()
        mediaPlayer_button.click()
    
    def select_video_view(self):
        mediaPlayer_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "VideoView")
    
        assert mediaPlayer_button.is_displayed()
        mediaPlayer_button.click()
    
    