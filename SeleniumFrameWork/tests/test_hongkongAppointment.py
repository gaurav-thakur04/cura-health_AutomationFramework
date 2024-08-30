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

    # // TC_03 : hongkong, apply for hospital readmission, medicare, 20/5/2019, this a comment

    @pytest.mark.run(order=5)
    def test_hongkongBooking(self):
        self.lf.clickOnMenuToggle()
        time.sleep(3)
        self.lf.clickOnLoginToggle()
        self.lf.clickOnUsernameBox()
        self.lf.clickOnPassword()
        time.sleep(3)
        self.lf.clickOnLoginButton()

        self.af.clickOnHongkongFacility()
        self.af.clickHospitalReadmission()
        self.af.clickOnMedicare()
        time.sleep(5)
        self.bp.sendText("14/8/2024","txt_visit_date", "id")
        self.bp.sendText("this is a comment", "txt_comment", "id")
        time.sleep(5)
        self.af.submitButton()

        expected_url = "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"

        assert expected_url == self.driver.current_url

        self.driver.close()