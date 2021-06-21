import configparser
import os

from open_project.tests.api_tests.rest.app_requests import RestRequests
from open_project.tests.api_tests.rest.rest_entities import OpenProjectEntities
from open_project.tests.api_tests.utilities.utilities import CommonUtilities


class BaseApiTestClass:
    config_parser = configparser.ConfigParser()
    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    config_parser.read(TEST_DIR + '\\..\\..\\env\\config.ini')

    domain = config_parser['env']['domain']
    api_token = config_parser['user']['api_token']

    entities = OpenProjectEntities()
    rest_requests = RestRequests(domain, api_token)

    common_utilities = CommonUtilities()
