from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import config_handler

CHROMEDRIVER_PATH = './drivers/chromedriver.exe'
INCOGNITO = '--incognito'

def create_driver():
    options = webdriver.ChromeOptions()
    if config_handler.get_incognito():
        options.add_argument(INCOGNITO)
    options.headless = config_handler.get_headless()
    service = Service(CHROMEDRIVER_PATH)
    return webdriver.Chrome(service=service,options=options)