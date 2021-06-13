import configparser

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject


class OpenProjectSanityTests:
    driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
    driver_wait: WebDriverWait = WebDriverWait(driver, 2)
    config_parser = configparser.ConfigParser()
    config_parser.read('../../env/config.ini')

    username = config_parser['user']['username']
    password = config_parser['user']['password']

    login_page_object = LoginPageObject(driver, driver_wait)
    login_page_object.goto_page()
    print()

    def test_login(self):
        self.login_page_object.fill_login_page("login", "pwd")


test = OpenProjectSanityTests()
