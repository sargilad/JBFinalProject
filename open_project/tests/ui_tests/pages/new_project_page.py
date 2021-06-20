from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class NewProjectPage(BasePage):
    textBox_name_locator = (By.CSS_SELECTOR, "#formly_3_textInput_name_0")
    button_advanced_settings_locator = (By.CLASS_NAME, "op-fieldset--toggle")

    textBox_description_locator = (By.CSS_SELECTOR,
                                   "#formly_9_formattableInput_description_1 >"
                                   " div > op-ckeditor > div > div.document-editor__editable-container > div")

    combo_status_locator = (By.CSS_SELECTOR, "#formly_9_selectProjectStatusInput__links\.status_4 input")

    list_status_locator = (By.CLASS_NAME, "ng-dropdown-panel-items")

    button_save_locator = (By.CSS_SELECTOR,
                           "#content > openproject-base > div > ui-view > op-new-project >"
                           " op-dynamic-form > form > div > button")

    def textbox_username_element(self) -> WebElement:
        return self.text_box_wrapper.get_element(self.textBox_name_locator)

    def button_advanced_settings_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_advanced_settings_locator)

    def textbox_description_element(self) -> WebElement:
        return self.text_box_wrapper.get_element(self.textBox_description_locator)

    def combo_status_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.combo_status_locator)

    def list_status_element(self) -> WebElement:
        return self.list_wrapper.get_element(self.list_status_locator)

    def button_save_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_save_locator)
