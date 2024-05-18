import pytest
from appium.webdriver.common.appiumby import AppiumBy
from screens.homeScreen import HomeScreen as onHomeScreen
# from screens.mediaScreen import MediaScreen as onMediaScreen


"""
APPIUM WITH PYTEST SET UP SCRIPT
"""


@pytest.mark.usefixtures('test_setup_android')
class TestMediaNavigation:
    def test_navigate_home_screen(self):
        homeMenuButtons = [
            "Access'ibility", 'Accessibility', 'Animation', 'App', 'Content', 'Graphics', 
            'Media', 'NFC', 'OS', 'Preference', 'Text', 'Views']
        
        for button in homeMenuButtons:
            onHomeScreen.select_option(self, button)
