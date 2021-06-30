from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from open_project.tests.api_tests.tests.test_api_base import BaseApiTestClass
from open_project.tests.api_tests.tests.test_flows import TestFlows
from open_project.tests.api_tests.utilities.common_wrappers import AssertionWrapper


@pytest.mark.proj_sanity
@allure.severity(severity_level=Severity.CRITICAL)
class TestProjectCrud(BaseApiTestClass):
    @allure.description("CREATE project test")
    def test_create_project(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name, description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)

        project = response.json()
        AssertionWrapper.assert_not_none(project)
        AssertionWrapper.assert_equals(actual=project['name'], expected=name)
        AssertionWrapper.assert_equals(actual=project['identifier'], expected=name)

    @allure.description("GET project test")
    def test_get_project(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name, description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()
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
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name, description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        description = "Updated description"
        body = self.entities.get_project_update_body(description=description)
        response = self.rest_requests.update_project(proj_id=project['id'], body=body)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.OK)

        project = response.json()
        AssertionWrapper.assert_not_none(project)
        AssertionWrapper.assert_equals(actual=project['description']['raw'], expected=description)

    @allure.description("DELETE project test")
    def test_delete_project(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name=name, description=description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        response = self.rest_requests.delete_project(proj_id=project['id'], body={})
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)

        response = self.rest_requests.get_single_project(proj_id=project['id'], expected_status=HTTPStatus.NOT_FOUND,
                                                         attempts=5)
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)


@pytest.mark.workpkg_sanity
class TestWorkPkg(BaseApiTestClass):
    @allure.description("CREATE work package test")
    def test_create_work_package(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name=name, description=description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        pkg_name = self.common_utilities.get_random_string(prefix="pkg_")
        response = TestFlows.create_work_package(self, pkg_name=pkg_name, project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.CREATED)

        pkg = response.json()
        AssertionWrapper.assert_not_none(pkg)
        AssertionWrapper.assert_equals(actual=pkg['subject'], expected=pkg_name)

    @allure.description("GET work package test")
    def test_get_work_package(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name=name, description=description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        pkg_name = self.common_utilities.get_random_string(prefix="pkg_")
        response = TestFlows.create_work_package(self, pkg_name=pkg_name, project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.CREATED)

        pkg = response.json()
        pkg_name = pkg['subject']

        response = self.rest_requests.get_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.OK)

        pkg = response.json()
        AssertionWrapper.assert_not_none(pkg)
        AssertionWrapper.assert_equals(actual=pkg['_links']['type']['title'], expected='Task')
        AssertionWrapper.assert_equals(actual=pkg['subject'], expected=pkg_name)

    @allure.description("UPDATE work package test")
    def test_update_work_package(self):
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name=name, description=description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        pkg_name = self.common_utilities.get_random_string(prefix="pkg_")
        response = TestFlows.create_work_package(self, pkg_name=pkg_name, project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.CREATED)

        pkg = response.json()

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
        name = self.common_utilities.get_random_string(prefix="proj-")
        description = "This is the first test project"
        response = TestFlows.create_project(self, name=name, description=description)
        AssertionWrapper.assert_equals(response.status_code, HTTPStatus.CREATED)
        project = response.json()

        pkg_name = self.common_utilities.get_random_string(prefix="pkg_")
        response = TestFlows.create_work_package(self, pkg_name=pkg_name, project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.CREATED)

        pkg = response.json()

        response = self.rest_requests.delete_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)

        response = self.rest_requests.get_work_package(pkg_id=pkg['id'])
        AssertionWrapper.assert_equals(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
