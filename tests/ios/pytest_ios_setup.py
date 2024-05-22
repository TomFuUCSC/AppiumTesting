import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSHomeScreen
from screens.iOS.homeScreen import HomeScreen as onHomeScreen


@pytest.mark.usefixtures('test_setup_ios')
class TestHomeNavigation:
    def test_navigate_home_screen(self): 
        for button in iOSHomeScreen.buttons:
            onHomeScreen.select_option(self, button)
            self.driver.back()
