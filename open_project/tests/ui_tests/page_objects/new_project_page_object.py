from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.new_project_page import NewProjectPage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.list_wrapper import ListWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class NewProjectPageObject(BasePageObject):
    text_box_wrapper: TextBoxWrapper
    button_wrapper: ButtonWrapper
    list_wrapper: ListWrapper
    new_project_page: NewProjectPage

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.new_project_page = NewProjectPage(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)
        self.list_wrapper = ListWrapper(driver, driver_wait)

    def fill_project_data(self):
        element = self.new_project_page.textbox_username_element()
        self.text_box_wrapper.send_keys(element, "new name")  # todo add random  value

        element = self.new_project_page.button_advanced_settings_element()
        self.button_wrapper.click_on_element(element)

        element = self.new_project_page.textbox_description_element()
        self.text_box_wrapper.send_keys(element, "Description")  # todo add random  value

        element = self.new_project_page.combo_status_element()
        self.button_wrapper.click_on_element(element)

        element = self.new_project_page.list_status_element()
        by_class_tuple = (By.CLASS_NAME, "project-status--name")
        self.list_wrapper.get_element_from_list_base_entity(element, by_class_tuple, "ON TRACK").click()

    def submit_new_project(self):
        element = self.new_project_page.button_save_element()
        self.button_wrapper.click_on_element(element)