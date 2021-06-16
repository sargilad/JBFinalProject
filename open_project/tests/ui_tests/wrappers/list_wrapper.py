from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.wrappers.base_entity_wrapper import BaseWrapper


class ListWrapper(BaseWrapper):
    def get_element_from_list(self, locator: tuple, text_to_search: str) -> WebElement:
        element_list = self.driver.find_elements(*locator)
        for element in element_list:
            element_text = element.text
            if text_to_search in element_text:
                return element
        return None

    def get_element_from_list_base_entity(self, parent_element: WebElement, locator: tuple,
                                          text_to_search: str) -> WebElement:
        element_list = parent_element.find_elements(*locator)
        for element in element_list:
            element_text = element.text
            if text_to_search in element_text:
                return element
        return None
