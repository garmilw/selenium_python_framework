import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class loginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _login_link = "SIGN IN"
    _username_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"
    _user_button = "//button[@class='btn btn-sm dropdown-toggle zl-navbar-rhs-btn']"
    _logout_link = "//div[@id='navbar-inverse-collapse']//a[@href='/logout']"

    # actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, "link")

    def enterEmail(self, email):
        self.sendKeys(email, self. _username_field, "id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, "id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "xpath")

    def login(self, email, password):
        self.logout()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)  # wait needed to avoid recaptcha
        self.clickLoginButton()

    def verifyLoginSucessful(self):
        result = self.isElementPresent("//div[@id='navbar-inverse-collapse']//a[@href='/mycourses']", "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='form-group has-error']", "xpath")
        return result

    def verifyTitle(self):
        # return self.verifyPageTitle("Let's Kode It")
        return self.verifyPageTitle("My Courses")

    def logout(self):
        if self.isElementPresent(self._user_button, "xpath"):
            self.elementClick(self._user_button, "xpath")
            self.elementClick(self._logout_link, "xpath")

