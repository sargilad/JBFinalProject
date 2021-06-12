import json
from http import HTTPStatus
from open_project.tests.base_test import BaseTestClass


class TestProjectCrudTests(BaseTestClass):
    def test_create_project(self) -> json:
        # create project
        name = super().common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        body = super().entities.get_project_create_body(project_name=name, description=description)
        project = super().rest_requests.create_project(body=body)
        assert project['name'] == name
        assert project['identifier'] == name

        return project

    def test_get_project(self):
        project = self.test_create_project()
        name = project['name']
        description = project['description']['raw']

        project = super().rest_requests.get_single_project(id=project['id'])
        assert project['name'] == name
        assert project['description']['raw'] == description

    def test_update_project(self):
        project = self.test_create_project()

        description = "Updated description"
        body = super().entities.get_project_update_body(description=description)
        project = super().rest_requests.update_project(id=project['id'], body=body)
        assert project['description']['raw'] == description

    def test_delete_project(self):
        project = self.test_create_project()

        status = super().rest_requests.delete_project(id=project['id'], body={})
        assert status == HTTPStatus.NO_CONTENT

        project = super().rest_requests.get_single_project(id=project['id'], expected_status=HTTPStatus.NOT_FOUND,
                                                           attempts=5)
        assert project == {}


class TestWorkPkgTest(BaseTestClass):
    test_project_crud_tests = TestProjectCrudTests()

    def test_create_work_package(self) -> json:
        project = self.test_project_crud_tests.test_create_project()

        pkg_name = super().common_utilities.get_random_string(prefix="pkg_")
        body = super().entities.get_create_work_package_body(pkg_name=pkg_name,
                                                             project_ref=project['_links']['self']['href'],
                                                             pkg_type="/api/v3/types/1")
        pkg = super().rest_requests.create_work_package(body=body)
        assert pkg['subject'] == pkg_name

        return pkg

    def test_get_work_package(self):
        pkg = self.test_create_work_package()
        pkg_name = pkg['subject']

        pkg = super().rest_requests.get_work_package(id=pkg['id'])
        assert pkg['_links']['type']['title'] == 'Task'
        assert pkg['subject'] == pkg_name

    def test_update_work_package(self):
        pkg = self.test_create_work_package()

        lock_version = pkg['lockVersion']
        package_description = "Package description updated"
        body = super().entities.get_work_package_update_body(lock_version=lock_version, description=package_description)
        pkg = super().rest_requests.update_work_package(id=pkg['id'], body=body)
        assert pkg['description']['raw'] == package_description

    def test_delete_work_package(self):
        pkg = self.test_create_work_package()

        status = super().rest_requests.delete_work_package(id=pkg['id'])
        assert status == HTTPStatus.NO_CONTENT

        pkg = super().rest_requests.get_work_package(id=pkg['id'])
        assert pkg == {}

tests = TestWorkPkgTest()
tests.test_update_work_package()
