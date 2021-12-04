from pages.courses.registercourses import RegisterCoursesPage
from utilities.result_status import ResultStatus
import unittest, pytest, time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.rs = ResultStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    # def setUp(self):
    #     #     self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    # @data(("JavaScript for beginners", "5001 1234 5678 1234", "1225", "444", "12345"), ("Learn Python 3 from scratch", "5102 9876 5432 1098", "1225", "444", "12345"))
    # @data(*getCSVData("c:\\projects\\python\\letskodeit\\testdata.csv"))
    @data(*getCSVData("testdata.csv"))   # this only works if the csv file is in the project folder
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, zipcode):
        self.courses.navToCourses()
        self.courses.enterCourseName(courseName)
        time.sleep(2)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(2)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=zipcode)
        result = self.courses.verifyEnrollFailed()
        self.rs.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

