import configparser
from open_project.tests.api_tests.rest.app_requests import RestRequests
from open_project.tests.api_tests.rest.rest_entities import OpenProjectEntities
from open_project.tests.api_tests.utilities.utilities import CommonUtilities


class BaseTestClass:
    config_parser = configparser.ConfigParser()
    config_parser.read('../env/config.ini')
    questions_sections_list = config_parser.sections()

    domain = config_parser['env']['domain']
    api_token = config_parser['user']['api_token']

    entities = OpenProjectEntities()
    rest_requests = RestRequests(domain, api_token)

    common_utilities = CommonUtilities()
