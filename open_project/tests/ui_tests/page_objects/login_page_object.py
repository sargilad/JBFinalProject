from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.login_page import LoginPage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class LoginPageObject(BasePageObject):
    login_page: LoginPage
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.login_page = LoginPage(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)

    def goto_page(self, domain: str):
        self.driver.get(domain + '/login')

    def fill_login_page(self, username: str, password: str):
        element = self.login_page.textbox_username_element()
        self.text_box_wrapper.send_keys(element, text=username)
        element = self.login_page.textbox_password_element()
        self.text_box_wrapper.send_keys(element, text=password)

    def submit_form(self):
        element = self.login_page.button_sign_in_element()
        self.button_wrapper.click_on_element(element)
