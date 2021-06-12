from open_project.tests.ui_tests.tests.ui_base_test import BaseUITestClass


class OpenProjectSanityTests(BaseUITestClass):

    def test_login(self):
        super().driver.get("https://jbfinal3.openproject.com/login")
        super().driver.find_element_by_id("username").send_keys("asdasdasd")
        super().driver.find_element_by_id("password").send_keys("asdasdasd")
        super().driver.find_element_by_css_selector("#login-form > form > input.button.-highlight").click()




test = OpenProjectSanityTests()
test.test_login()