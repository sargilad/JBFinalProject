import configparser

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.api_tests.utilities.utilities import CommonUtilities


class BaseUITestClass:
    driver: webdriver
    driver_wait: WebDriverWait
    config_parser: configparser
    username: str
    password: str
    domain: str

    common_utilities = CommonUtilities()

    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read('../../env/config.ini')
        self.domain = self.config_parser['env']['domain']
        self.username = self.config_parser['user']['username']
        self.password = self.config_parser['user']['password']
        wait_timeout = self.config_parser['env']['wait_timeout']

        self.driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
        self.driver_wait: WebDriverWait = WebDriverWait(driver=self.driver, timeout=int(wait_timeout))
