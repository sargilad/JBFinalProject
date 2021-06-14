from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from open_project.tests.ui_tests.pages.base_page import BasePage


class AddNewProjectPage(BasePage):
    textBox_name_locator = (By.CSS_SELECTOR, "#formly_3_textInput_name_0")
    button_advanced_settings_locator = (
        By.CSS_SELECTOR, "#content > openproject-base > "
                         "div > ui-view > op-new-project > op-dynamic-form >"
                         " form > formly-form > formly-field:nth-child(3) > "
                         "op-dynamic-field-group-wrapper > fieldset > legend > button")

    textBox_description_locator = (By.CSS_SELECTOR,
                                   "#formly_9_formattableInput_description_1 >"
                                   " div > op-ckeditor > div > div.document-editor__editable-container > div")

    combo_status_selector = (By.CSS_SELECTOR, "#formly_9_selectProjectStatusInput__links\.status_4 > div")

    button_save_locator = (By.CSS_SELECTOR,
                           "#content > openproject-base > div > ui-view > op-new-project > op-dynamic-form > form > div > button")

    def textbox_username_element(self) -> WebElement:
        return self.text_box_wrapper.get_element(self.textBox_username_locator)

    def button_advanced_settings_element(self) -> WebElement:
        return self.button_wrapper.get_element(self.button_advanced_settings_locator)

    def combo_status_element(self) -> WebElement:
        pass

    def button_save_element(self) -> WebElement:
        self.button_wrapper.get_element(self.button_save_locator).click()
