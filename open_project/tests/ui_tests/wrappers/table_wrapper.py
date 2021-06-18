from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.wrappers.base_entity_wrapper import BaseWrapper


class TableWrapper(BaseWrapper):

    def get_table_rows(self, table_element: WebElement, locator: tuple = (By.TAG_NAME, "tr")) -> list:
        elements_list = table_element.find_elements(*locator)
        return elements_list

    def get_cell_value_from_table(self, table_element: WebElement, row: int, column: str) -> str:
        elements_list = self.get_table_rows(table_element)
        text = str(elements_list[row].text).replace("\n"," ").split(" ")
        if(column.upper() == "SUBJECT" ):
            return text[1]
        elif(column.upper() == "TYPE" ):
            return text[2]
        else:
            return ""

        print()
