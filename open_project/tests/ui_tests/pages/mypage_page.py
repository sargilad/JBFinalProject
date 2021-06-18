from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class MyPagePage(BasePage):
    button_add_locator = (By.CLASS_NAME, "icon-add")
    list_app_menu_locator = (By.ID, "quick-add-menu")
    drop_down_projects_list_locator = (By.CLASS_NAME, "op-app-menu--item-title")
    list_projects_locator = (By.CLASS_NAME, "project-menu-autocomplete--wrapper")

    def button_add_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_add_locator)

    def list_app_menu_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_app_menu_locator)

    def drop_down_projects_list_element(self):
        return self.button_wrapper.get_element(self.drop_down_projects_list_locator)

    def list_projects_element(self):
        return self.list_wrapper.get_element(self.list_projects_locator)