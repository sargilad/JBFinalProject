from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class WorkPackagesPage(BasePage):
    button_add_locator = (By.CLASS_NAME, "wp-create-button")
    list_work_type_locator = (By.ID, "types-context-menu")
    table_work_packages_locator = (By.CLASS_NAME, "results-tbody")
    list_menu_root_locator = (By.CLASS_NAME, "collapsible-menu--results-container")

    def button_add_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_add_locator)

    def list_work_type_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_work_type_locator)

    def table_work_packages_element(self) -> WebElement:
        return self.table_wrapper.get_element(self.table_work_packages_locator)

    def list_menu_root_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_menu_root_locator)
