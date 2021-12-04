from base.selenium_driver import seleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class ResultStatus(seleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(ResultStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("*** Verification Successful: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("*** Verification Failed: " + resultMessage)
                    self.screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("*** Verification Failed - No Result: " + resultMessage)
                self.screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("*** Exception Occurred while setting test status!! ***")
            self.screenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

