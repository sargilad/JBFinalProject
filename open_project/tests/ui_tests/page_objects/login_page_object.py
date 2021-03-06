import allure
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

    @allure.step("Init LoginPageObject")
    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.login_page = LoginPage(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)

    @allure.step("Navigate to Login page")
    def goto_page(self, domain: str):
        self.driver.get(domain + '/login')

    @allure.step("Fill Login form with data")
    def fill_login_page(self, username: str, password: str):
        self.text_box_wrapper.wait_for_element_presence(self.login_page.textBox_username_locator)
        element = self.login_page.textbox_username_element()
        self.text_box_wrapper.send_keys(element, text=username)
        element = self.login_page.textbox_password_element()
        self.text_box_wrapper.send_keys(element, text=password)

    @allure.step("Submit Login form")
    def submit_form(self):
        self.button_wrapper.wait_for_element_presence(self.login_page.button_sign_in_locator)
        element = self.login_page.button_sign_in_element()
        self.button_wrapper.click_on_element(element=element)
