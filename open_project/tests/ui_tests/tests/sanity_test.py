from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject
from open_project.tests.ui_tests.tests.ui_base_test import BaseUITestClass


class OpenProjectSanityTests(BaseUITestClass):
    login_page_object: LoginPageObject


    def __init__(self):
        super().__init__()


        self.login_page_object = LoginPageObject(self.driver, self.driver_wait)

    def test_login(self):
        self.login_page_object.goto_page(self.domain)

        self.login_page_object.fill_login_page(username=self.username, password=self.password)


test = OpenProjectSanityTests()
test.test_login()
