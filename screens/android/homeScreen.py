from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class HomeScreen(Base):
    def select_option(self, label):
        AppAction.click_button(self, label)
        
    def navigate_to_light_theme_control_screen(self):
        AppAction.click_button(self, "Views")
        AppAction.click_button(self, "Controls")
        AppAction.click_button(self, "1. Light Theme")
        
