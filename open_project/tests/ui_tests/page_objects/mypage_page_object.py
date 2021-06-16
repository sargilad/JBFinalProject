from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.mypage_page import MyPagePage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.list_wrapper import ListWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class MyPagePageObject(BasePageObject):
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper
    list_wrapper: ListWrapper
    my_page_page: MyPagePage

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.my_page_page = MyPagePage(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)
        self.list_wrapper = ListWrapper(driver, driver_wait)

    def wait_for_page_to_load(self):
        locator = self.my_page_page.button_add_locator
        self.button_wrapper.wait_for_element(locator)

    def open_new_project_page(self):
        element = self.my_page_page.button_add_element()
        self.button_wrapper.click_on_element(element)

        list_element = self.my_page_page.list_app_menu_element()
        self.list_wrapper.get_element_from_list_base_entity(base_entity=list_element,
                                                            locator=self.my_page_page.by_list_tag_locator,
                                                            text_to_search="Project").click()
