import time
from enum import Enum
from http import HTTPStatus

import allure
from requests import Response
from requests.auth import HTTPBasicAuth

from open_project.tests.api_tests.rest.client import RestClient


class RestRequests:
    base_url = ''
    projects_url = ''
    work_pkg_url = ''
    rest_client: RestClient
    basic_auth: HTTPBasicAuth

    def __init__(self, domain: str, basic_auth: HTTPBasicAuth):
        self.rest_client = RestClient(basic_auth)
        self.base_url = domain + "/api/v3"
        self.projects_url = self.base_url + "/projects/"
        self.work_pkg_url = self.base_url + "/work_packages/"
        self.basic_auth = basic_auth

    """Creating new project"""

    @allure.step("creating new project")
    def create_project(self, body) -> Response:
        response = self.rest_client.post(url=self.projects_url, body=body,
                                         headers_list=self._build_request_header())
        print(f"project created: {response.json()}")
        return response

    """retrieving project data"""

    @allure.step("querying project")
    def get_single_project(self, proj_id: int, expected_status: int = HTTPStatus.OK, attempts: int = 1) -> Response:
        response = None
        attempt = 1
        while attempt <= attempts:
            response = self.rest_client.get(url=self.projects_url + str(proj_id),
                                            headers_list=self._build_request_header())
            if response.status_code == expected_status:
                break
            else:
                attempt += 1
                print("attempt")
                time.sleep(1)

        return response

    """Updating project data"""

    @allure.step("updating project")
    def update_project(self, proj_id, body) -> Response:
        response = self.rest_client.patch(url=self.projects_url + str(proj_id), body=body,
                                          headers_list=self._build_request_header())
        print(f"project PATCH: {response.json()}")
        return response

    """Deleting project"""

    @allure.step("deleting project")
    def delete_project(self, proj_id, body) -> Response:
        response = self.rest_client.delete(url=self.projects_url + str(proj_id), body=body,
                                           headers_list=self._build_request_header())
        return response

    @allure.step("creating new work package")
    def create_work_package(self, body) -> Response:
        response = self.rest_client.post(url=self.work_pkg_url, body=body,
                                         headers_list=self._build_request_header())
        print(f"package CREATE: {response.json()}")
        return response

    @allure.step("querying work package")
    def get_work_package(self, pkg_id: int) -> Response:
        response = self.rest_client.get(url=self.work_pkg_url + str(pkg_id),
                                        headers_list=self._build_request_header())
        print(f"package GET: {response.json()}")
        return response

    @allure.step("updating work package")
    def update_work_package(self, pkg_id, body) -> Response:
        response = self.rest_client.patch(url=self.work_pkg_url + str(pkg_id), body=body,
                                          headers_list=self._build_request_header())
        print(f"package UPDATE: {response.json()}")
        return response

    @allure.step("deleting work package")
    def delete_work_package(self, pkg_id: int, body: dict = {}) -> Response:
        response = self.rest_client.delete(url=self.work_pkg_url + str(pkg_id), body=body,
                                           headers_list=self._build_request_header())
        return response

    def _build_request_header(self) -> dict:
        return {self._HeadersEnum.CONTENT_TYPE.value: self._HeadersEnum.APPLICATION_JSON.value}

    class _HeadersEnum(Enum):
        CONTENT_TYPE = 'Content-type'
        APPLICATION_JSON = 'application/json; charset=UTF-8'
        AUTHORIZATION = 'Authorization'
