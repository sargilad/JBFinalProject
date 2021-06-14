from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.mypage_page import MyPagePage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class MyPagePageObject(BasePageObject):
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper
    my_page_page: MyPagePage

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.my_page_page = MyPagePage(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)

    def wait_for_page_to_load(self):
        locator = self.my_page_page.button_add_locator
        self.button_wrapper.wait_for_element(locator)

    # def open
