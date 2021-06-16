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
            return None

    def wait_for_element(self, by: By):
        try:
            self.driver_wait.until(method=EC.presence_of_element_located(by))
        except TimeoutException as toe:
            print(toe)
            return None

    def click_on_element(self, button_element: WebElement):
        try:
            button_element.click()
        except ElementNotVisibleException as enve:
            print(enve)
        except StaleElementReferenceException as ser:
            print(ser)
        except Exception as e:
            print(e)
