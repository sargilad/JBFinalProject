import configparser
import json
from http import HTTPStatus

from open_project.tests.api_tests.rest.app_requests import RestRequests
from open_project.tests.api_tests.rest.rest_entities import OpenProjectEntities
from open_project.tests.api_tests.utilities.utilities import CommonUtilities

config_parser = configparser.ConfigParser()
config_parser.read('../env/config.ini')
questions_sections_list = config_parser.sections()

domain = config_parser['env']['domain']
api_token = config_parser['user']['api_token']

entities = OpenProjectEntities()
rest_requests = RestRequests(domain, api_token)


def test_create_project() -> json:
    # create project
    name = CommonUtilities.get_random_string(prefix="proj_")
    description = "This is the first test project"
    body = entities.get_project_create_body(project_name=name, description=description)
    project = rest_requests.create_project(body)
    assert project['name'] == name
    # assert project['identifier'] == name #todo fix

    return project


def test_get_project():
    project = test_create_project()
    name = project['name']
    description = project['description']['raw']

    project = rest_requests.get_single_project(id=project['id'])
    assert project['name'] == name
    assert project['description']['raw'] == description


def test_update_project():
    project = test_create_project()

    description = "Updated description"
    body = entities.get_project_update_body(description=description)
    project = rest_requests.update_project(project['id'], body)
    assert project['description']['raw'] == description


def test_delete_project():
    project = test_create_project()

    status = rest_requests.delete_project(id=project['id'], body={})
    assert status == HTTPStatus.NO_CONTENT

    project = rest_requests.get_single_project(id=project['id'], expected_status=HTTPStatus.NOT_FOUND, attempts=5)
    assert project == {}


def test_create_work_package() -> json:
    project = test_create_project()

    pkg_name = CommonUtilities.get_random_string(prefix="pkg_")
    body = entities.get_create_work_package_body(pkg_name=pkg_name,
                                                 project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
    pkg = rest_requests.create_work_package(body=body)
    assert pkg['subject'] == pkg_name

    return pkg


def test_get_work_package():
    pkg = test_create_work_package()
    pkg_name = pkg['subject']

    pkg = rest_requests.get_work_package(id=pkg['id'])
    assert pkg['_links']['type']['title'] == 'Task'
    assert pkg['subject'] == pkg_name


def test_update_work_package():
    pkg = test_create_work_package()

    lock_version = pkg['lockVersion']
    package_description = "Package description updated"
    body = entities.get_work_package_update_body(lock_version=lock_version, description=package_description)
    pkg = rest_requests.update_work_package(id=pkg['id'], body=body)
    assert pkg['description']['raw'] == package_description


def test_delete_work_package():
    pkg = test_create_work_package()

    status = rest_requests.delete_work_package(id=pkg['id'])
    assert status == HTTPStatus.NO_CONTENT

    pkg = rest_requests.get_work_package(id=pkg['id'])
    assert pkg == {}


