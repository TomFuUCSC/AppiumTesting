import pytest
from os import environ
from appium import webdriver
from utils.data import Project
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function')
def test_setup_android(request):
    test_name = request.node.name
    build = environ.get('BUILD', "Pytest Android Sample")
    caps = {}
    caps["deviceName"] = 'Pixel_6_Pro'
    caps["platformName"] = 'Android'
    caps["platformVersion"] = '13'
    caps["app"] = f"{Project.app}"
    caps["isRealMobile"] = True
    caps['project'] = f"{Project.name}"
    caps['build'] = build
    caps['name'] = test_name
    driver = webdriver.Remote(Project.appium_server_url, options=UiAutomator2Options().load_capabilities(caps))
    request.cls.driver = driver
    
    yield driver
    driver.quit()