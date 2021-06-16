from selenium.webdriver.common.by import By

from open_project.tests.ui_tests.pages.base_page import BasePage


class ProjectPage(BasePage):
    header_overview_locator = (By.CSS_SELECTOR,
                               "#content > openproject-base > div > ui-view > "
                               "openproject-base > div > ui-view > overview > div > div > div > h2")

    def header_overview_element(self):
        return self.base_wrapper.get_element(self.header_overview_locator)
