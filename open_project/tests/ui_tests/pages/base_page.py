from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: webdriver = None
    driver_wait: WebDriverWait = None

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.driver_wait = driver_wait

