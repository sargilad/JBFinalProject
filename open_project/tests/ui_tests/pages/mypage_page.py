from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class MyPagePage(BasePage):
    button_add_locator = (By.CLASS_NAME, "icon-add")

    # textBox_password_locator = (By.CSS_SELECTOR, "#password")
    # button_sign_in_locator = (By.CSS_SELECTOR, "#login-form > form > input.button.-highlight")

    def button_add_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_add_locator)

    # def textbox_password_element(self) -> WebElement:
    #     return self.text_box_wrapper.get_element(self.textBox_password_locator)

    # def button_sign_in_element(self) -> WebElement:
    #     return self.text_box_wrapper.get_element(self.button_sign_in_locator)
