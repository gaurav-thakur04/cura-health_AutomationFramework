from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import SeleniumFrameWork.utilities.CustomLogger as cl

class WebDriverClass:

    log = cl.customLogger()
    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            PATH = (r"C:/Users/Lenovo/Documents/sel_python/chromedriver-win64/chromedriver.exe")
            service = Service(executable_path=PATH)
            driver = webdriver.Chrome(service=service)
            self.log.info("Chrome browser initializing")


        else:
            return f"{browserName} is not supporting Currently this project"

        return driver