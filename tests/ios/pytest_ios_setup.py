import pytest
from conftest_ios import test_setup_ios
# from screens.homeScreen import HomeScreen as onHomeScreen
from helpers.app_actions import AppAction
# from utils.data import HomeScreen


@pytest.mark.usefixtures('test_setup_ios')
class TestHomeNavigation:
    def test_navigate_home(self):
        AppAction.click_button('Activity Indicators')