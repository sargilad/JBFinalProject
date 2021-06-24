import allure
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWrapper:
    driver: webdriver = None
    driver_wait: WebDriverWait = None

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.driver_wait = driver_wait

    def get_element(self, by: tuple) -> WebElement:
        try:
            return self.driver.find_element(*by)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=e)

    def wait_for_element_presence(self, by: By):
        try:
            self.driver_wait.until(method=EC.presence_of_element_located(by))
        except TimeoutException as toe:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=toe)

    def wait_for_url_contains(self, url_substr: str):
        try:
            self.driver_wait.until(method=EC.url_contains(url_substr))
        except TimeoutException as toe:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=toe)

    def wait_for_element_visible(self, by: By):
        try:
            self.driver_wait.until(method=EC.visibility_of_element_located(by))
        except TimeoutException as toe:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=toe)

    def wait_for_element_clickable(self, by: By):
        try:
            self.driver_wait.until(method=EC.element_to_be_clickable(by))
        except TimeoutException as toe:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=toe)

    def click_on_element(self, element: WebElement):
        try:
            element.click()
        except ElementNotVisibleException as enve:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=enve)

        except StaleElementReferenceException as ser:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=ser)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(msg=e)

    def click_on_element_js(self, element: WebElement):
        self.driver.execute_script("arguments[0].click();", element)
