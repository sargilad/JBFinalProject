import configparser
import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from open_project.tests.api_tests.utilities.utilities import CommonUtilities
from open_project.tests.ui_tests.page_objects.login_page_object import LoginPageObject
from open_project.tests.ui_tests.page_objects.mypage_page_object import MyPagePageObject
from open_project.tests.ui_tests.page_objects.new_project_page_object import NewProjectPageObject
from open_project.tests.ui_tests.page_objects.new_work_package_page_object import NewWorkPackagePageObject
from open_project.tests.ui_tests.page_objects.project_page_object import ProjectPageObject
from open_project.tests.ui_tests.page_objects.work_package_page_object import WorkPackagesPageObject


class BaseUITestClass:
    driver: webdriver
    driver_wait: WebDriverWait
    config_parser: configparser
    username: str
    password: str
    domain: str

    login_page_object: LoginPageObject
    my_page_page_object: MyPagePageObject
    new_project_page_object: NewProjectPageObject
    project_page_object: ProjectPageObject
    work_packages_page_object: WorkPackagesPageObject
    new_work_package_page_object: NewWorkPackagePageObject

    common_utilities = CommonUtilities()

    @pytest.fixture()
    def init_test(self):
        self.config_parser = configparser.ConfigParser()
        TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        self.config_parser.read(TEST_DIR + '\\..\\..\\env\\config.ini')
        self.domain = self.config_parser['env']['domain']
        self.username = self.config_parser['user']['username']
        self.password = self.config_parser['user']['password']
        wait_timeout = self.config_parser['env']['wait_timeout']

        self.driver = webdriver.Chrome(executable_path=TEST_DIR + '\\..\\..\\resources\\chromedriver.exe')
        self.driver_wait: WebDriverWait = WebDriverWait(driver=self.driver, timeout=int(wait_timeout))

        self.login_page_object = LoginPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.my_page_page_object = MyPagePageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.new_project_page_object = NewProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.project_page_object = ProjectPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.work_packages_page_object = WorkPackagesPageObject(driver=self.driver, driver_wait=self.driver_wait)
        self.new_work_package_page_object = NewWorkPackagePageObject(driver=self.driver, driver_wait=self.driver_wait)

        yield
        self.driver.quit()
