import json
from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from open_project.tests.api_tests.tests.test_api_base import BaseApiTestClass
from open_project.tests.api_tests.utilities.common_wrappers import AssertionWrapper


@pytest.mark.proj_sanity
@allure.severity(severity_level=Severity.CRITICAL)
class TestProjectCrud(BaseApiTestClass):
    @allure.description("CREATE project test")
    def test_create_project(self) -> json:
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        body = self.entities.get_project_create_body(project_name=name, description=description)
        response = self.rest_requests.create_project(body=body)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)

        project = response.json()
        AssertionWrapper.assert_not_none(project)
        AssertionWrapper.assert_equals(actual=project['name'], expected=name)
        AssertionWrapper.assert_equals(actual=project['identifier'], expected=name)

        return project

    @allure.description("GET project test")
    def test_get_project(self):
        project = self.test_create_project()
        name = project['name']
        description = project['description']['raw']

        response = self.rest_requests.get_single_project(proj_id=project['id'])
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.OK)

        project = response.json()
        AssertionWrapper.assert_not_none(project)
        AssertionWrapper.assert_equals(actual=project['name'], expected=name)
        AssertionWrapper.assert_equals(actual=project['description']['raw'], expected=description)

    @allure.description("UPDATE project test")
    def test_update_project(self):
        project = self.test_create_project()

        description = "Updated description"
        body = self.entities.get_project_update_body(description=description)
        response = self.rest_requests.update_project(proj_id=project['id'], body=body)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.OK)

        project = response.json()
        AssertionWrapper.assert_not_none(project)
        AssertionWrapper.assert_equals(actual=project['description']['raw'], expected=description)

    @allure.description("DELETE project test")
    def test_delete_project(self):
        project = self.test_create_project()

        response = self.rest_requests.delete_project(proj_id=project['id'], body={})
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)

        response = self.rest_requests.get_single_project(proj_id=project['id'], expected_status=HTTPStatus.NOT_FOUND,
                                                         attempts=5)
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)


@pytest.mark.workpkg_sanity
class TestWorkPkg(BaseApiTestClass):
    test_project_crud_tests = TestProjectCrud()

    @allure.description("CREATE work package test")
    def test_create_work_package(self) -> json:
        project = self.test_project_crud_tests.test_create_project()

        pkg_name = self.common_utilities.get_random_string(prefix="pkg_")
        body = self.entities.get_create_work_package_body(pkg_name=pkg_name,
                                                          project_ref=project['_links']['self']['href'],
                                                          pkg_type="/api/v3/types/1")
        response = self.rest_requests.create_work_package(body=body)
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.CREATED)

        pkg = response.json()
        AssertionWrapper.assert_not_none(pkg)
        AssertionWrapper.assert_equals(actual=pkg['subject'], expected=pkg_name)

        return pkg

    @allure.description("GET work package test")
    def test_get_work_package(self):
        pkg = self.test_create_work_package()
        pkg_name = pkg['subject']

        response = self.rest_requests.get_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.OK)

        pkg = response.json()
        AssertionWrapper.assert_not_none(pkg)
        AssertionWrapper.assert_equals(actual=pkg['_links']['type']['title'], expected='Task')
        AssertionWrapper.assert_equals(actual=pkg['subject'], expected=pkg_name)

    @allure.description("UPDATE work package test")
    def test_update_work_package(self):
        pkg = self.test_create_work_package()

        lock_version = pkg['lockVersion']
        package_description = "Package description updated"
        body = self.entities.get_work_package_update_body(lock_version=lock_version, description=package_description)
        response = self.rest_requests.update_work_package(pkg_id=pkg['id'], body=body)
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.OK)

        pkg = response.json()
        AssertionWrapper.assert_not_none(pkg)
        assert pkg['description']['raw'] == package_description

    @allure.description("DELETE work package test")
    def test_delete_work_package(self):
        pkg = self.test_create_work_package()

        response = self.rest_requests.delete_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)

        response = self.rest_requests.get_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
