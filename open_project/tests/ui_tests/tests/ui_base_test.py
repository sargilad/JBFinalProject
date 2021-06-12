import configparser
from selenium import webdriver
from open_project.tests.api_tests.utilities.utilities import CommonUtilities


class BaseUITestClass:
    driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
    config_parser = configparser.ConfigParser()
    config_parser.read('../../env/config.ini')

    username = config_parser['user']['username']
    password = config_parser['user']['password']

    common_utilities = CommonUtilities()
