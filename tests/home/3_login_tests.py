from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driverService = Service("C:\\Projects\\Python\\SeleniumTraining\\webdrivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=driverService)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, "SIGN IN")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("garmilw@gmail.com")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("automation")

        time.sleep(2)

        loginButton = driver.find_element(By.XPATH, "//input[@type='submit']")
        loginButton.click()

        time.sleep(2)

        myCourses = driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/mycourses']")
        if myCourses is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        driver.quit()

ff = LoginTests()
ff.test_validLogin()