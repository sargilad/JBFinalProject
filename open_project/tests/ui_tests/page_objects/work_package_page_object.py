from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.work_packages_page import WorkPackagesPage
from open_project.tests.ui_tests.wrappers.button_wrapper import ButtonWrapper
from open_project.tests.ui_tests.wrappers.list_wrapper import ListWrapper


class WorkPackagesPageObject(BasePageObject):
    work_packages_page: WorkPackagesPage
    button_wrapper: ButtonWrapper
    list_wrapper: ListWrapper

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.work_packages_page = WorkPackagesPage(driver, driver_wait)
        self.button_wrapper = ButtonWrapper(driver, driver_wait)
        self.list_wrapper = ListWrapper(driver, driver_wait)

    def open_new_work_page(self):
        self.button_wrapper.wait_for_element_presence(self.work_packages_page.button_add_locator)
        element = self.work_packages_page.button_add_element()
        self.button_wrapper.click_on_element(button_element=element)

        self.list_wrapper.wait_for_element_presence(self.work_packages_page.list_work_type_locator)
        list_element = self.work_packages_page.list_work_type_element()
        self.list_wrapper.get_element_from_list_base_entity(parent_element=list_element,
                                                            locator=self.work_packages_page.by_list_tag_locator,
                                                            text_to_search="TASK").click()
