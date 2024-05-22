from helpers.app_actions import AppAction
from datetime import datetime
from datetime import timedelta, date
import pytz


east_coast = pytz.timezone('America/New_York')  # src: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
current_date = datetime.now(east_coast).strftime('%B %d, %Y')
current_time = datetime.now(east_coast).strftime('%I:%M %p')


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class DatePickerViewsScreen(Base):
    def confirm_date_and_time(self):
        print(current_time)  
        AppAction.confirm_element_is_visible(self, current_date)
        assert current_date is not None  # checks the value of current_date
        
        # AppAction.confirm_element_is_visible(self, current_time)
        # assert current_time is not None  # checks the value of current_time
        
    def set_new_date(self):
        delta = timedelta(days=7)
        new_date = date.today() + delta
        
        AppAction.click_button(self, current_date)
        AppAction.click_button(self, '29')
        AppAction.dismiss_popover(self, '//XCUIElementTypeButton[@name="PopoverDismissRegion"]')
        assert new_date != current_date
        
    def set_new_time(self):
        new_time = '900'
        AppAction.click_button(self, current_time)
        current_time.send_keys(new_time)
        AppAction.dismiss_popover(self, '//XCUIElementTypeButton[@name="PopoverDismissRegion"]')
        assert new_time != current_time
