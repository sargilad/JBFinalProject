from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class BasePage:
    driver: webdriver = None
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)
