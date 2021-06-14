from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePageObject:
    driver: webdriver
    driver_wait: WebDriverWait
    domain:str

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.driver_wait = driver_wait


