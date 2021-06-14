import configparser

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseUITestClass:
    driver: webdriver
    driver_wait: WebDriverWait
    config_parser: configparser
    username: str
    password: str
    domain: str

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
        self.driver_wait: WebDriverWait = WebDriverWait(self.driver, 2)
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read('../../env/config.ini')

        self.domain = self.config_parser['env']['domain']
        self.username = self.config_parser['user']['username']
        self.password = self.config_parser['user']['password']
