import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from SeleniumFrameWork.pages.LoginPage import LogInForm
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.utilities.CustomLogger import customLogger
from SeleniumFrameWork.utilities import XLUtils
import time

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class Test_DDT_Login(unittest.TestCase):
    #baseUrl = ReadConfig.getApplicationURL()
    path = r"C:\Users\Lenovo\PycharmProjects\CuraHealth\SeleniumFrameWork\testData\Cura_Login_Data.xlsx"

    #logger = LogGen.loggen()

    @pytest.fixture(autouse=True)  # to use the objects throughout the class, conftest driver object treated as class object
    def classObjects(self):
        self.lf = LogInForm(self.driver)
        self.bp = BaseClass(self.driver)
        self.cl = customLogger()

    @pytest.mark.run(order=2)
    def test_login_ddt(self):

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in a Excel:", self.rows)

        lst_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lf.clickOnBookAppointment()

            self.driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds

            self.bp.setUserName(self.user)
            self.bp.setPassword(self.password)
            self.lf.clickOnLoginButton()
            time.sleep(5)

            message = self.driver.find_elements(By.TAG_NAME, "h2")[0].text

            exp_message = "Make Appointment"

            if message == exp_message:
                if self.exp == "Pass":
                    self.cl.info("**** Passed ****")
                    self.lf.clickOnMenuToggle()
                    self.lf.clickOnLogoutButton()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.cl.info("**** Failed ****")
                    self.lf.clickOnMenuToggle()
                    self.lf.clickOnLogoutButton()
                    lst_status.append("Fail")
            elif message != exp_message:  # Passing invalid data
                if self.exp == "Pass":  # it is a conflict
                    self.cl.info("**** Failed ****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.cl.info("**** Passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.cl.info("**** Login DDT test passed ****")
            self.driver.close()

            assert True
        else:
            self.cl.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False
        print(lst_status)
        print(message)
        self.cl.info("******** End of Login DDT Test ***************")
        self.cl.info("***************** Competed Login DDT***************")


