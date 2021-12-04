import time
from pages.home.login_page import loginPage
import unittest
import utilities.custom_logger as cl
import logging
import pytest
from utilities.result_status import ResultStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = loginPage(self.driver)
        self.ts = ResultStatus(self.driver)
        self.log = cl.customLogger(logging.DEBUG)
        self.log.info("-" * 30)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("garmilw@gmail.com", "automation")

        time.sleep(2)

        result1 = self.lp.verifyTitle()
        if result1:
            self.ts.mark(result1, "Title verified")
        else:
            self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verifyLoginSucessful()
        if result2:
            self.ts.markFinal("test_ValidLogin", result2, "Login Successful")
        else:
            self.ts.markFinal("test_ValidLogin", result2, "Login Failed")


    @pytest.mark.run(order=2)
    def test_verifyLoginFailed(self):
        self.lp.login("test@example", "abcdef")

        time.sleep(2)

        result = self.lp.verifyLoginFailed()
        if result:
            self.ts.markFinal("test_verifyLoginFailed", result, "Login Failed as expected with invalid credentials")
        else:
            self.ts.markFinal("test_verifyLoginFailed", result, "Login Successful with invalid credentials")

