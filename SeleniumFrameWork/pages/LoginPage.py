from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl

class LogInForm(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    #locators values in login Page

    _menuToggle = "menu-toggle" #id
    _makeAppointmentButton = "btn-make-appointment"  #id
    _loginMenuToggle = "//*[@id='sidebar-wrapper']/ul/li[3]/a" #xpath
    _userName = "txt-username"  #id
    _passWord = "txt-password"  #id
    _logInButton = "btn-login"  #id
    _logOutButton = "Logout"  #link

    def clickOnMenuToggle(self):
        self.clickOnElement(self._menuToggle, "id")
        cl.allureLogs("Clicked on Menu")

    def clickOnBookAppointment(self):
        self.clickOnElement(self._makeAppointmentButton, "id")
        cl.allureLogs("Clicked on BookAppointment")

    def clickOnLoginToggle(self):
        self.clickOnElement(self._loginMenuToggle, "xpath")
        cl.allureLogs("Clicked on Login Button")

    def clickOnUsernameBox(self):
        self.sendText("John Doe", self._userName, "id")
        cl.allureLogs("Entered Username")


    def clickOnPassword(self):
        self.sendText("ThisIsNotAPassword", self._passWord, "id")
        cl.allureLogs("Entered Password")


    def clickOnLoginButton(self):
        self.clickOnElement(self._logInButton, "id")
        cl.allureLogs("Clicked on LoginButton")

    def clickOnLogoutButton(self):
        self.clickOnElement(self._logOutButton , "link")
        cl.allureLogs("Clicked on LogoutButton")


