from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    textBox_username_locator = By.NAME("username")
    textBox_password_locator = By.NAME("password")
    button_sign_in_locator = By.CSS_SELECTOR("#login-form > form > input.button.-highlight")

    def textbox_username_element(self) -> WebElement:
        return super().driver.findElement(self.textBox_username_locator)

    def textbox_password_element(self) -> WebElement:
        return super().driver.findElement(self.textBox_password_locator)

    def button_sign_in_element(self) -> WebElement:
        return super().driver.findElement(self.button_sign_in_locator)
