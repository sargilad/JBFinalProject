import configparser
import time
from http import HTTPStatus

from app_requests import RestRequests
from rest_entities import OpenProjectEntities
from utilities import CommonUtilities

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')
questions_sections_list = config_parser.sections()

domain = config_parser['env']['domain']
api_token = config_parser['user']['api_token']


def main():
    entities = OpenProjectEntities()
    rest_requests = RestRequests(domain, api_token)

    # create project
    name = CommonUtilities.get_random_string(prefix="proj_")
    description = "This is the first test project"
    body = entities.get_project_create_body(project_name=name, description=description)
    project = rest_requests.create_project(body)
    # Assert
    # project['name'] == name
    # project['identifier'] == name

    # Get project
    tic = time.perf_counter()
    project = rest_requests.get_single_project(id=project['id'])
    toc = time.perf_counter()
    # Assert
    # project['name'] == name
    # project['description']['raw'] == description)

    # Update project
    description = "This is a project description"
    body = entities.get_project_update_body(description=description)
    project = rest_requests.update_project(project['id'], body)
    # Assert
    # project['description']['raw'] == description)

    # Delete project
    status = rest_requests.delete_project(id=project['id'], body={})
    # Check status == HTTPStatus.NO_CONTENT

    project = rest_requests.get_single_project(id=project['id'], expected_status=HTTPStatus.NOT_FOUND, attempts=5)
    # Assert project = {}

    # Create work package
    body = entities.get_project_create_body(project_name=CommonUtilities.get_random_string(prefix="proj_"))
    project = rest_requests.create_project(body)

    pkg_name = CommonUtilities.get_random_string(prefix="pkg_")
    body = entities.get_create_work_package_body(pkg_name=pkg_name,
                                                 project_ref=project['_links']['self']['href'],
                                                 pkg_type="/api/v3/types/1")
    pkg = rest_requests.create_work_package(body=body)
    # pkg['subject'] == name

    # GET work package
    pkg = rest_requests.get_work_package(id=pkg['id'])
    # task and package
    # pkg['_links']['type']['title'] == 'Task'
    # pkg['subject'] == pkg_name

    # update work package
    lock_version = pkg['lockVersion']
    package_description = "This is a package description"
    body = entities.get_work_package_update_body(lock_version=lock_version, description=package_description)
    pkg = rest_requests.update_work_package(id=pkg['id'], body=body)
    # pkg['description']['raw'] == package_description

    # delete work package
    status = rest_requests.delete_work_package(id=pkg['id'])
    # Check status == HTTPStatus.NO_CONTENT

    pkg = rest_requests.get_work_package(id=pkg['id'])
    # Assert pkg={}


if __name__ == '__main__':
    main()
