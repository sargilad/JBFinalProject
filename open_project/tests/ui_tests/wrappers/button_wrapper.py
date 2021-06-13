from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from open_project.tests.ui_tests.wrappers.base_wrapper import BaseWrapper


class ButtonWrapper(BaseWrapper):

    def click(self, driver: webdriver, by: By):
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by))
            driver.findElement(by).click()
        except StaleElementReferenceException as ser:
            # retry finding the element in the refreshed dome
            driver.findElement(by).click()
        except Exception as e:
            print(f"Element identified by {str(by)} was not clickable after 10 seconds")
