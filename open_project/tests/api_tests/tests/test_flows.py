from requests import Response

from open_project.tests.api_tests.tests.test_api_base import BaseApiTestClass


class TestFlows:

    def create_project(self, name: str, description: str) -> Response:
        body = self.entities.get_project_create_body(project_name=name, description=description)
        return self.rest_requests.create_project(body=body)

    def create_work_package(self, name: str, proj_ref: str, pkg_type: str) -> Response:
        body = self.entities.get_create_work_package_body(pkg_name=name,
                                                          project_ref=proj_ref,
                                                          pkg_type=pkg_type)
        return self.rest_requests.create_work_package(body=body)
