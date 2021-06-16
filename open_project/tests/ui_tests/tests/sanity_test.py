from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject
from open_project.tests.ui_tests.page_objects.mypage_page_object import MyPagePageObject
from open_project.tests.ui_tests.page_objects.new_project_page_object import NewProjectPageObject
from open_project.tests.ui_tests.tests.ui_base_test import BaseUITestClass


class OpenProjectSanityTests(BaseUITestClass):
    login_page_object: LoginPageObject
    my_page_page_object: MyPagePageObject
    new_project_page_object = NewProjectPageObject

    def __init__(self):
        super().__init__()

        self.login_page_object = LoginPageObject(self.driver, self.driver_wait)
        self.my_page_page_object = MyPagePageObject(self.driver, self.driver_wait)
        self.new_project_page_object = NewProjectPageObject(self.driver, self.driver_wait)

    def test_login(self):
        # login page
        self.login_page_object.goto_page(self.domain)
        self.login_page_object.fill_login_page(username=self.username, password=self.password)
        self.login_page_object.submit_form()
        # todo add wait

        # Home page
        self.my_page_page_object.wait_for_page_to_load()
        self.my_page_page_object.open_new_project_page()
        # todo add wait

        # Add New project
        self.new_project_page_object.fill_project_data()  # todo optional send data to class
        self.new_project_page_object.submit_new_project()


test = OpenProjectSanityTests()
test.test_login()
