import configparser

from requests.auth import HTTPBasicAuth

from open_project.tests.api_tests.rest.app_requests import RestRequests
from open_project.tests.api_tests.rest.rest_entities import OpenProjectEntities
from open_project.tests.api_tests.utilities.utilities import CommonUtilities
from open_project.tests.env import conf_def


class BaseApiTestClass:
    config_parser = configparser.ConfigParser()
    config_parser.read(conf_def.CONF_DIR + '\\config.ini')
    domain = config_parser['env']['domain']
    api_token = config_parser['user']['api_token']
    entities = OpenProjectEntities()
    common_utilities = CommonUtilities()
    rest_requests = RestRequests(domain=domain, basic_auth=HTTPBasicAuth(username="apikey",
                                                                         password=api_token))
