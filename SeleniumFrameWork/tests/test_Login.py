import unittest
import pytest
import time

from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.LoginPage import LogInForm

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class LogInTest(unittest.TestCase):

    @pytest.fixture(autouse=True)  #to use the objects throughout the class, conftest driver object treated as class object
    def classObjects(self):
        self.lf = LogInForm(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.lf.clickOnMenuToggle()
        time.sleep(3)
        self.lf.clickOnLoginToggle()
        self.lf.clickOnUsernameBox()
        self.lf.clickOnPassword()
        time.sleep(3)
        self.lf.clickOnLoginButton()

        expected_url = "https://katalon-demo-cura.herokuapp.com/#appointment"

        assert expected_url == self.driver.current_url

        self.lf.clickOnMenuToggle()
        self.lf.clickOnLogoutButton()



