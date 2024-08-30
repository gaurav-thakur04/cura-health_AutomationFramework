import unittest
import pytest
import time

from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.LoginPage import LogInForm
from SeleniumFrameWork.pages.AppontmentPage import AppointmentForm

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class BookAppointment(unittest.TestCase):

    @pytest.fixture(autouse=True)  #to use the objects throughout the class, conftest driver object treated as class object
    def classObjects(self):
        self.lf = LogInForm(self.driver)
        self.bp = BaseClass(self.driver)
        self.af = AppointmentForm(self.driver)

    # TC_02 : tokyo, apply for hospital readmission, medicare, 14/2/2020, this a comment

    @pytest.mark.run(order=3)
    def test_tokyoBooking(self):
        self.lf.clickOnMenuToggle()
        time.sleep(3)
        self.lf.clickOnLoginToggle()
        self.lf.clickOnUsernameBox()
        self.lf.clickOnPassword()
        time.sleep(3)
        self.lf.clickOnLoginButton()

        self.af.clickOnTokyoFacility()
        self.af.clickHospitalReadmission()
        self.af.clickOnMedicare()
        time.sleep(5)
        self.bp.sendText("14/2/2020","txt_visit_date", "id")
        self.bp.sendText("this is a comment", "txt_comment", "id")
        time.sleep(5)
        self.af.submitButton()

        expected_url = "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"

        assert expected_url == self.driver.current_url

        self.driver.close()