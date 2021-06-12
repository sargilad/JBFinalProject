import time
from enum import Enum
from http import HTTPStatus

from api_factory import RestClient
import json


class RestRequests:
    projects_url = ''
    work_pkg_url = ''
    rest_client = None
    api_token = ''

    def __init__(self, domain: str, api_token: str):
        self.rest_client = RestClient()
        self.projects_url = domain + "api/v3/projects/"
        self.work_pkg_url = domain + "api/v3/work_packages/"
        self.api_token = api_token

    def create_project(self, body) -> json:
        try:
            response = self.rest_client.post(url=self.projects_url, body=body,
                                             headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.CREATED:
                print(f"project CREATE: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_single_project(self, id: int, expected_status: int = HTTPStatus.OK, attempts: int = 1) -> json:
        try:
            response = None
            attempt = 1
            while attempt <= attempts:
                response = self.rest_client.get(url=self.projects_url + str(id),
                                                headers_list=self._build_request_header())
                if response.status_code == expected_status:
                    break
                else:
                    attempt += 1
                    print("attempt")
                    time.sleep(1)

            if response.status_code == HTTPStatus.OK:
                print(f"project GET: {response.json()}")
                return response.json()
            elif response.status_code == HTTPStatus.NOT_FOUND:
                print(f"Project id {id} not found")
                return {}
        except Exception as e:
            print(e)
            return None

    def update_project(self, id, body):
        try:
            response = self.rest_client.patch(url=self.projects_url + str(id), body=body,
                                              headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"project PATCH: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def delete_project(self, id, body) -> int:
        try:
            response = self.rest_client.delete(url=self.projects_url + str(id), body=body,
                                               headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.NO_CONTENT:
                print(f"project deleted")
                return HTTPStatus.NO_CONTENT
        except Exception as e:
            print(e)
            return HTTPStatus.EXPECTATION_FAILED

    def create_work_package(self, body) -> json:
        try:
            response = self.rest_client.post(url=self.work_pkg_url, body=body,
                                             headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.CREATED:
                print(f"package CREATE: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def get_work_package(self, id: int) -> json:
        try:
            response = self.rest_client.get(url=self.work_pkg_url + str(id), headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"package GET: {response.json()}")
                return response.json()
            elif response.status_code == HTTPStatus.NOT_FOUND:
                print(f"package id {id} not found")
                return {}
        except Exception as e:
            print(e)
            return None  # might cause NPE

    def update_work_package(self, id, body):
        try:
            response = self.rest_client.patch(url=self.work_pkg_url + str(id), body=body,
                                              headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.OK:
                print(f"package PATCH: {response.json()}")
                return response.json()
        except Exception as e:
            print(e)
            return None

    def delete_work_package(self, id: int, body: dict = {}) -> int:
        try:
            response = self.rest_client.delete(url=self.work_pkg_url + str(id), body=body,
                                               headers_list=self._build_request_header())
            if response.status_code == HTTPStatus.NO_CONTENT:
                print(f"Work package deleted")
                return HTTPStatus.NO_CONTENT
        except Exception as e:
            print(e)
            return HTTPStatus.EXPECTATION_FAILED

    def _build_request_header(self) -> dict:
        return {self._HeadersEnum.AUTHORIZATION.value: 'Basic ' + self.api_token,
                self._HeadersEnum.CONTENT_TYPE.value: self._HeadersEnum.APPLICATION_JSON.value}

    class _HeadersEnum(Enum):
        CONTENT_TYPE = 'Content-type'
        APPLICATION_JSON = 'application/json; charset=UTF-8'
        AUTHORIZATION = 'Authorization'
