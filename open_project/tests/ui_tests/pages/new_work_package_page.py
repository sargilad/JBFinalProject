from selenium.webdriver.common.by import By

from open_project.tests.ui_tests.pages.base_page import BasePage


class NewWorkPackagePage(BasePage):
    text_box_package_name_locator = (By.ID, "wp-new-inline-edit--field-subject")
    text_box_description_locator = (By.CSS_SELECTOR, ".document-editor__editable")
    button_save_locator = (By.ID, "work-packages--edit-actions-save")

    def text_box_package_name_element(self):
        return self.text_box_wrapper.get_element(self.text_box_package_name_locator)

    def text_box_description_element(self):
        return self.text_box_wrapper.get_element(self.text_box_description_locator)

    def button_save_element(self):
        return self.button_wrapper.get_element(self.button_save_locator)
