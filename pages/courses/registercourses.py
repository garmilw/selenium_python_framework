import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
# from base.webdriverfactory import getbaseurl


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "//input[@id='search']"
    _search_course_icon = "//button[@class='find-course search-course']"
    _course = "//div[@class='zen-course-title dynamic-text']//h4[contains(@text,'{0}')]"
    _all_courses = "//a[@href='/courses']"
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']"
    # /parent::div
    _course_iframe = "courses-iframe"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.elementClick(locator=self._search_box, locatorType="xpath")
        self.clearField(locator=self._search_box, locatorType="xpath")
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_course_icon, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        # self.switchToFrame(name="__privateStripeFrame11")
        self.SwitchFrameByIndex(self._zip, locatorType="name")
        self.sendKeys(zip, locator=self._zip, locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        # self.enterZip(zip)

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, zip)
        # self.clickAgreeToTermsCheckbox()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result

    def navToCourses(self):
        # in case the test case failed and left the browser on a different page, return to starting point
        # self.driver.get(self.baseURL)
        self.switchToDefaultContent()
        self.scrollIntoView(locator=self._course_iframe)
        self.switchToFrame(id=self._course_iframe)

