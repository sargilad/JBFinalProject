from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.pages.login_page import LoginPage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class LoginPageObject:
    driver: webdriver
    driver_wait: WebDriverWait
    login_page: LoginPage
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.driver_wait = driver_wait
        self.login_page = LoginPage(driver)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)

    def goto_page(self):
        self.driver.get("http://www.ynet.co.il")

    def fill_login_page(self, username: str, password: str):
        element = self.login_page.textbox_username_element()
        self.text_box_wrapper.send_keys(element, text=username)
        element = self.login_page.textbox_password_element()
        self.text_box_wrapper.send_keys(element, text=password)

    def submit_form(self):
        self.button_wrapper.click(self.driver, LoginPage.button_sign_in_locator)
