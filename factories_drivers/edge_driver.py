from selenium import webdriver
from selenium.webdriver.edge.service import Service
from utils import config_handler

EDGEDRIVER_PATH = './drivers/msedgedriver.exe'
INCOGNITO = '--incognito'

def create_driver():
    service = Service(EDGEDRIVER_PATH)
    options = webdriver.EdgeOptions()
    if config_handler.get_incognito():
        options.add_argument(INCOGNITO)
    options.headless = config_handler.get_headless()
    return webdriver.Edge(service=service,options=options)