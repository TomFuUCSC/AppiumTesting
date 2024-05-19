import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSHomeScreen
from helpers.app_actions import AppAction
from screens.homeScreen import HomeScreen as onHomeScreen


@pytest.mark.usefixtures('test_setup_ios')
class TestHomeNavigation:
    def test_navigate_home_screen(self): 
        for button in iOSHomeScreen.buttons:
            onHomeScreen.select_option(self, button)
            self.driver.back()
            
    def test_navigate_to_text_input_section(self):
        AppAction.click_button(self, "Text Fields")
