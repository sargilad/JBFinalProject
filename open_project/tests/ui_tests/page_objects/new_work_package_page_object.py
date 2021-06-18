from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.new_work_package_page import NewWorkPackagePage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.text_box_wrapper import TextBoxWrapper


class NewWorkPackagePageObject(BasePageObject):
    new_work_package_page: NewWorkPackagePage
    button_wrapper: ButtonWrapper
    text_box_wrapper: TextBoxWrapper

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.new_work_package_page = NewWorkPackagePage(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)
        self.text_box_wrapper = TextBoxWrapper(driver, driver_wait)

    def fill_new_package_data(self, package_name: str, description: str = "Description"):
        self.text_box_wrapper.wait_for_element_presence(self.new_work_package_page.text_box_package_name_locator)
        element = self.new_work_package_page.text_box_package_name_element()
        self.text_box_wrapper.send_keys(web_element=element, text=package_name)

        self.text_box_wrapper.wait_for_element_visible(self.new_work_package_page.text_box_description_locator)
        element = self.new_work_package_page.text_box_description_element()
        self.text_box_wrapper.send_keys(web_element=element, text=description)

    def submit_new_package(self):
        self.button_wrapper.wait_for_element_presence(self.new_work_package_page.button_save_locator)
        element = self.new_work_package_page.button_save_element()
        self.button_wrapper.click_on_element(button_element=element)
