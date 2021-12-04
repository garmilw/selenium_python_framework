from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.chrome.service import Service as ChromeService

class WebDriverFactory():

    baseURL = "https://courses.letskodeit.com/practice"

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        if self.browser == 'firefox':
            print("Running tests on firefox")
            driverService = FFService("C:\\Projects\\Python\\webdrivers\\geckodriver.exe")
            driver = webdriver.Firefox(service=driverService)
        else:
            print("Running tests on chrome")
            driverService = ChromeService("C:\\Projects\\Python\\webdrivers\\chromedriver.exe")
            driver = webdriver.Chrome(service=driverService)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(self.baseURL)
        return driver

    def getbaseurl(self):
        return self.baseURL


