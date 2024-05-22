from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class HomeScreen(Base):
    def select_option(self, label):
        AppAction.click_button(self, label)
        
