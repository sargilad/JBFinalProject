from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.wrappers.base_entity_wrapper import BaseWrapper


class TextBoxWrapper(BaseWrapper):

    @staticmethod
    def send_keys(web_element: WebElement, text: str):
        if text is not None:
            try:
                web_element.send_keys(text)
            except StaleElementReferenceException as ser:
                print(ser)
            except Exception as e:
                print(e)
