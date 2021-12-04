from base.selenium_driver import seleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(seleniumDriver):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return titleToVerify == actualTitle
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
