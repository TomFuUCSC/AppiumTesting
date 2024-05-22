from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class ButtonViewsScreen(Base):
    def click_on_button(self, label):
        AppAction.click_button(self, label)