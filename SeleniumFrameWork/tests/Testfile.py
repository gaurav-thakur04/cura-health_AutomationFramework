from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SeleniumFrameWork.base.DriverClass import WebDriverClass
from SeleniumFrameWork.base.BasePage import BaseClass
import time
import SeleniumFrameWork.utilities.CustomLogger as cl
from SeleniumFrameWork.pages.LoginPage import LogInForm


wd = WebDriverClass()


driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)
lf = LogInForm(driver)
bp.launchWebPage("https://katalon-demo-cura.herokuapp.com/","CURA Healthcare Service")

lf.clickOnMenuToggle()
lf.clickOnLoginToggle()
lf.clickOnUsernameBox()
lf.clickOnPassword()
lf.clickOnLoginButton()
message = driver.find_elements(By.TAG_NAME,"h2")[0].text
print(message)
assert message == "Make Appointment"


#below the block of code will help in negative testing
#without password and username , and correct and incorrect combination of username and password
"""
driver.find_element(By.ID,"txt-username").send_keys("Joe rogan")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
lf.clickOnLoginButton()
message = driver.find_elements(By.TAG_NAME,"p")[1].text
print(message)
assert message == "Login failed! Please ensure the username and password are valid."
"""

"""
lf.clickOnMenuToggle()
bp.clickOnElement("Logout","link")
"""


time.sleep(5)
driver.quit()




"""


# data driven testing negative testing
"""