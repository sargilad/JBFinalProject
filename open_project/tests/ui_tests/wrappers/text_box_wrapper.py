from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.wrappers.base_wrapper import BaseWrapper


class TextBoxWrapper(BaseWrapper):

    def send_keys(self, web_element: WebElement, text: str):
        if text is not None:
            web_element.send_keys(text)
