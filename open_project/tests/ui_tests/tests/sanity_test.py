from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject
from open_project.tests.ui_tests.page_objects.mypage_page_object import MyPagePageObject
from open_project.tests.ui_tests.page_objects.new_project_page_object import NewProjectPageObject
from open_project.tests.ui_tests.page_objects.project_page_object import ProjectPageObject
from open_project.tests.ui_tests.tests.ui_base_test import BaseUITestClass


# @pytest.mark.sanity
class TestOpenProjectSanityTests(BaseUITestClass):
    login_page_object: LoginPageObject
    my_page_page_object: MyPagePageObject
    new_project_page_object: NewProjectPageObject
    project_page_object: ProjectPageObject

    def __init__(self):
        super().__init__()

        self.login_page_object = LoginPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.my_page_page_object = MyPagePageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.new_project_page_object = NewProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.project_page_object = ProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)

    def test_create_project_sanity(self):
        # login page
        self.login_page_object.goto_page(domain=self.domain)
        self.login_page_object.fill_login_page(username=self.username, password=self.password)
        self.login_page_object.submit_form()

        # Home page
        self.my_page_page_object.open_new_project_page()

        # Add New project
        proj_name = self.common_utilities.get_random_string(prefix="proj-")
        proj_description = self.common_utilities.get_random_string(str_length=50)
        self.new_project_page_object.fill_project_data(project_name=proj_name,
                                                       description=proj_description)
        self.new_project_page_object.submit_new_project()

        # validate project created
        self.project_page_object.wait_for_page_ready()

        project_name_created = self.my_page_page_object.get_project_name_from_drop_down()
        assert project_name_created == proj_name


test = TestOpenProjectSanityTests()
test.test_create_project_sanity()
