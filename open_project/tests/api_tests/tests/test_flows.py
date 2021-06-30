from requests import Response

from open_project.tests.api_tests.tests.test_api_base import BaseApiTestClass


class TestFlows:

    def create_project(self: BaseApiTestClass, name: str, description: str) -> Response:
        body = self.entities.get_project_create_body(project_name=name, description=description)
        return self.rest_requests.create_project(body=body)

    def create_work_package(self: BaseApiTestClass, pkg_name: str, project_ref: str, pkg_type: str) -> Response:
        body = self.entities.get_create_work_package_body(pkg_name=pkg_name,
                                                          project_ref=project_ref,
                                                          pkg_type=pkg_type)
        return self.rest_requests.create_work_package(body=body)
