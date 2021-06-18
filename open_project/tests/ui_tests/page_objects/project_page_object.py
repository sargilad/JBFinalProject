from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.project_page import ProjectPage
from open_project.tests.ui_tests.wrappers.base_entity_wrapper import BaseWrapper


class ProjectPageObject(BasePageObject):
    project_page: ProjectPage
    base_wrapper: BaseWrapper

    project_name: str = ""

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        super().__init__(driver, driver_wait)
        self.project_page = ProjectPage(driver, driver_wait)
        self.base_wrapper = BaseWrapper(driver, driver_wait)

    def wait_for_page_ready(self):
        self.base_wrapper.wait_for_element(self.project_page.header_overview_locator)

    def set_project_name(self, name: str):
        self.project_name = name

    def get_project_name(self):
        return self.project_name
