from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Service
from utils import config_handler

FIREFOXDRIVER_PATH = './drivers/geckodriver.exe'
FIREFOX_PATH = 'C:/Program Files/Mozilla Firefox/firefox.exe'
PRIVATE_MODE = 'browser.privatebrowsing.autostart'

def create_driver():
    service = Service(FIREFOXDRIVER_PATH)
    options = webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile()
    profile.set_preference(PRIVATE_MODE,config_handler.get_incognito())
    options.binary_location = FIREFOX_PATH
    options.headless = config_handler.get_headless()
    return webdriver.Firefox(service=service,options=options)

    
    
