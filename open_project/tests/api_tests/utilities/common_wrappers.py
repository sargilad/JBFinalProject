import allure


class AssertionWrapper:

    @staticmethod
    @allure.step
    def assert_equals(actual, expected, resume_after_fail: bool = False):
        try:
            assert actual == expected
        except AssertionError as ae:
            if not resume_after_fail:
                raise AssertionError(ae)

    @staticmethod
    @allure.step
    def assert_not_none(entity, resume_after_fail: bool = False):
        try:
            assert entity is not None
        except AssertionError as ae:
            if not resume_after_fail:
                raise AssertionError(ae)
