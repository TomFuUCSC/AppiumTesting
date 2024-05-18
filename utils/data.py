class Device:
    name = 'Pixel_6_Pro'
    platformName = 'Android',
    platformVersion = '13',
    name = 'Pixel_6_Pro',
    automationName = 'uiautomator2',
    language = 'en',
    locale = 'US'
    
    
class Project:
    appium_server_url = 'http://127.0.0.1:4723'
    app = '/Users/pablovergara/Desktop/automation/hyacinth/apps/android/ApiDemos-debug.apk'
    name = "Android Pytest"
    
    
class HomeScreen:
    buttons = [
        "Access'ibility", 'Accessibility', 'Animation', 'App', 'Content', 'Graphics', 
        'Media', 'NFC', 'OS', 'Preference', 'Text', 'Views']
    
    
class Accessibility:
    accessibility_node_provider_copy = "Enable TalkBack and Explore-by-touch from accessibility settings. Then touch the colored squares."