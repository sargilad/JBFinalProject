from open_project.tests.ui_tests.page_objects.base_page_object import BasePageObject
from open_project.tests.ui_tests.pages.login_page import LoginPage


class LoginPageObject(BasePageObject):
    login_page = LoginPage()

    def fill_login_page(self, username:str, password:str):
        element = self.login_page.textbox_username_element()

        element = self.login_page.textbox_password_element()

    def submit_form(self):
        pass



