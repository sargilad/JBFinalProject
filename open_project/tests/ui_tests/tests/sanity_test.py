import pytest

from open_project.tests.api_tests.utilities.enums import WorkPackageType, SideMenuItems, WorkPackagesTableHeaders
from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject
from open_project.tests.ui_tests.page_objects.mypage_page_object import MyPagePageObject
from open_project.tests.ui_tests.page_objects.new_project_page_object import NewProjectPageObject
from open_project.tests.ui_tests.page_objects.new_work_package_page_object import NewWorkPackagePageObject
from open_project.tests.ui_tests.page_objects.project_page_object import ProjectPageObject
from open_project.tests.ui_tests.page_objects.work_package_page_object import WorkPackagesPageObject
from open_project.tests.ui_tests.tests.ui_base_test import BaseUITestClass


@pytest.mark.sanity
class TestOpenProjectSanityTests(BaseUITestClass):
    login_page_object: LoginPageObject
    my_page_page_object: MyPagePageObject
    new_project_page_object: NewProjectPageObject
    project_page_object: ProjectPageObject
    work_packages_page_object: WorkPackagesPageObject
    new_work_package_page_object: NewWorkPackagePageObject

    def __init__(self):
        super().__init__()

        self.login_page_object = LoginPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.my_page_page_object = MyPagePageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.new_project_page_object = NewProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.project_page_object = ProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.work_packages_page_object = WorkPackagesPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.new_work_package_page_object = NewWorkPackagePageObject(driver=self.driver, driver_wait=self.driver_wait)

    def test_create_project_sanity(self) -> str:
        # login page
        self.login_page_object.goto_page(domain=self.domain)
        self.login_page_object.fill_login_page(username=self.username, password=self.password)
        self.login_page_object.submit_form()

        # Add New project
        self.my_page_page_object.open_new_project_page()
        proj_name = self.common_utilities.get_random_string(prefix="proj-")
        proj_description = self.common_utilities.get_random_string(str_length=50)
        self.new_project_page_object.fill_project_data(project_name=proj_name,
                                                       description=proj_description)
        self.new_project_page_object.submit_new_project()

        # validate project created
        self.project_page_object.wait_for_page_ready()
        project_name_created = self.my_page_page_object.get_project_name_from_drop_down()
        assert project_name_created == proj_name
        self.project_page_object.set_project_name(proj_name)

    def test_create_work_package_sanity(self):
        # Create new project
        self.test_create_project_sanity()
        project_name = self.project_page_object.get_project_name()

        # Navigate to work packages
        self.my_page_page_object.select_project_from_list(project_name)  # todo investigate
        self.project_page_object.select_from_side_menu(SideMenuItems.WORK_PACKAGES.value)
        work_packages_count_before = self.work_packages_page_object.get_packages_table_rows_count()

        # create new task
        self.work_packages_page_object.open_new_work_package_page(WorkPackageType.TASK.value)
        work_pkg_title = self.new_work_package_page_object.get_new_work_package_title()
        assert work_pkg_title == "New " + WorkPackageType.TASK.value
        task_subject = "pkg1"
        self.new_work_package_page_object.fill_new_work_package_data(task_subject, "Package description")
        self.new_work_package_page_object.submit_new_package()

        # Verify rows # incremented by 1
        self.work_packages_page_object.wait_for_work_package_page()
        self.work_packages_page_object.select_from_side_menu(SideMenuItems.ALL_OPEN.value)
        work_packages_count_after = self.work_packages_page_object.get_packages_table_rows_count()
        assert work_packages_count_after - work_packages_count_before == 1

        # verify subject and type
        task_type_created = self.work_packages_page_object. \
            get_element_from_work_packages_table(0, WorkPackagesTableHeaders.TYPE.value)
        assert task_type_created == WorkPackageType.TASK.value
        task_subject_created = self.work_packages_page_object. \
            get_element_from_work_packages_table(0, WorkPackagesTableHeaders.SUBJECT.value)
        assert task_subject_created == task_subject


test = TestOpenProjectSanityTests()
test.test_create_work_package_sanity()
print("done")
