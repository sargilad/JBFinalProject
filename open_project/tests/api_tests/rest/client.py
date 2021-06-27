import requests
from requests import Response

from open_project.tests.api_tests.utilities import consts


class RestClient:
    def __init__(self):
        pass

    def get(self, url: str, headers_list: dict) -> Response:
        return requests.get(url, headers=headers_list, timeout=consts.WAIT)

    def post(self, url: str, body: dict, headers_list: dict) -> Response:
        return requests.post(url=url, json=body, headers=headers_list, timeout=consts.WAIT)

    def patch(self, url: str, body: dict, headers_list: dict) -> Response:
        return requests.patch(url=url, json=body, headers=headers_list, timeout=consts.WAIT)

    def delete(self, url: str, body: dict, headers_list: dict) -> Response:
        return requests.delete(url=url, json=body, headers=headers_list, timeout=consts.WAIT)
