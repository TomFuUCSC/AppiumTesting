import pytest
from screens.homeScreen import HomeScreen as onHomeScreen
from utils.data import HomeScreen, Accessibility
from helpers.app_actions import AppAction


"""
APPIUM WITH PYTEST SET UP SCRIPT
"""


@pytest.mark.usefixtures('test_setup_android')
class TestHomeNavigation:
    def test_navigate_home_screen(self): 
        for button in HomeScreen.buttons:
            onHomeScreen.select_option(self, button)
            self.driver.back()
            
    def test_navigate_to_accessibility_node_provider(self):
        AppAction.click_button(self, "Access'ibility")
        AppAction.click_button(self, 'Accessibility Node Provider')
        assert Accessibility.accessibility_node_provider_copy is not None
        
    def test_navigate_to_accessibility_check_list(self):
        AppAction.click_button(self, "Access'ibility")
        AppAction.click_button(self, 'Accessibility Node Querying')
        # TODO - move this to a page object w. assertion
        
    def test_navigate_to_accessibility_service(self):
        AppAction.click_button(self, "Access'ibility")
        AppAction.click_button(self, 'Accessibility Service')
        # TODO - move this to a page object w. assertion
        
    def test_navigate_to_accessibility_custom_view(self):
        AppAction.click_button(self, "Access'ibility")
        AppAction.click_button(self, 'Custom View')
        # TODO - move this to a page object w. assertion
