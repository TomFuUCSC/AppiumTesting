from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class AlertViewsScreen(Base):
    def select_alert_view(self, label):
        AppAction.click_button(self, label)
        
    def click_on_alert_action(self, action):
        AppAction.alert_action(self, action)
        
    def confirm_simple_alert(self, simple_alert):
        title_text = 'A Short Title Is Best'
        AppAction.alert_is_visible(self, simple_alert)
        AppAction.confirm_alert_title(self, title_text)
        
    def confirm_ok_cancel_alert(self, ok):   
        title_text = 'A Short Title Is Best'
        AppAction.alert_is_visible(self, ok)
        AppAction.confirm_alert_title(self, title_text)
        
    def submit_text_in_alert_input(self, text_input, text_value):
        AppAction.enter_text(self, text_input, text_value)
        
    def click_action_on_sheet(self, action):
        AppAction.sheet_action(self, action)
        
    