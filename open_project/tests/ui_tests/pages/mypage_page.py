from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class MyPagePage(BasePage):
    button_add_locator = (By.CLASS_NAME, "icon-add")
    list_app_menu_locator = (By.ID, "quick-add-menu")

    def button_add_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_add_locator)

    def list_app_menu_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_app_menu_locator)
