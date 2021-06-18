from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class WorkPackagesPage(BasePage):
    button_add_locator = (By.CLASS_NAME, "wp-create-button")
    list_work_type_locator = (By.ID, "types-context-menu")

    def button_add_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_add_locator)

    def list_work_type_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_work_type_locator)
