from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.wrappers.base_entity_wrapper import BaseWrapper


class TableWrapper(BaseWrapper):

    def get_table_rows(self, table_element: WebElement, locator: tuple = (By.TAG_NAME, "tr")) -> int:
        elements_list = table_element.find_elements(*locator)
        return elements_list
