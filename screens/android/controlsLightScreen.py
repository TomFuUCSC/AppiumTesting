from helpers.app_actions import AppAction
from appium.webdriver.common.appiumby import AppiumBy
import time


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
                
class LightThemeControlScreen(Base):     
    def checkUI(self):
        save_button = 'io.appium.android.apis:id/button'
        textfield = 'io.appium.android.apis:id/edit'
        off_switch = 'io.appium.android.apis:id/toggle1'
        ddl_planets = 'io.appium.android.apis:id/spinner1'
        
        AppAction.confirm_element_by_ID_is_visible(self, save_button)
        AppAction.confirm_element_by_ID_is_visible(self, textfield)
        AppAction.confirm_element_is_visible(self, 'Checkbox 1')
        AppAction.confirm_element_is_visible(self, 'Checkbox 2')
        AppAction.confirm_element_is_visible(self, 'RadioButton 1')
        AppAction.confirm_element_is_visible(self, 'RadioButton 2')
        AppAction.confirm_element_is_visible(self, 'Star')
        AppAction.confirm_element_by_ID_is_visible(self, off_switch)
        AppAction.confirm_element_by_ID_is_visible(self, ddl_planets)
        AppAction.confirm_element_is_visible(self, 'textColorPrimary')
        AppAction.confirm_element_is_visible(self, 'textColorSecondary')
        AppAction.confirm_element_is_visible(self, 'textColorTertiary')
    
    def click_save_button(self, ):
        AppAction.click_button_by_id(self, 'io.appium.android.apis:id/button')
        
    def enter_text(self, text_value):
        input = self.driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit')
        input.click()
        input.send_keys(text_value)
        
    def click_checkbox(self, label):
        AppAction.click_button(self, label)
        
    def click_radio_button(self, label):
        AppAction.click_button(self, label)
        
    def click_favorite(self):
        AppAction.click_button(self, 'Star')

    def click_off_switch1(self):
        AppAction.click_button_by_id(self, 'io.appium.android.apis:id/toggle1')
        
    def click_off_switch2(self):
        AppAction.click_button_by_id(self, 'io.appium.android.apis:id/toggle2')
        
    def select_from_list(self):
        ddl_planets = self.driver.find_element(AppiumBy.ID, 'android:id/text1')
        assert ddl_planets.text == "Mercury"
        ddl_planets.click()
        time.sleep(0.25)
        
        opt_earth = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[3]')
        opt_earth.click()
        
        updated_ddl = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Spinner/android.widget.TextView')
        assert updated_ddl.text == "Earth"