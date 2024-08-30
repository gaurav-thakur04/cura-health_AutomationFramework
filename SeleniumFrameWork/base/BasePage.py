from traceback import print_stack
import allure
from allure_commons.types import AttachmentType
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import SeleniumFrameWork.utilities.CustomLogger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url , title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web page launched with url " + url)
        except:
            self.log.info("Web page not launched with url " + url)
            print_stack()
            assert False

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator type" + locatorType + "entered is not found")
            return False

    def getWebElement(self, locatorValue, locatorType = "id"):
        webElement = True
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info("Webelement found with locator value" + locatorValue + "using locator type" + locatorByType)
        except:
            self.log.error("Webelement not found with locator value" + locatorValue + "using locator type" + locatorByType)
            print_stack()
            assert False
        return webElement


    def waitForElement(self, locatorValue, locatorType = "id"):
        webElement = True
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("Webelement found with locator value" + locatorValue + "using locator type" + locatorByType)

        except:
            self.log.error("Webelement not found with locator value" + locatorValue + "using locator type" + locatorByType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement


    def clickOnElement(self, locatorValue, locatorType = "id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info("Clicked on Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
        except:
            self.log.error("Not Clicked on Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
            print_stack()
            assert False

    def sendText(self, text, locatorValue, locatorType = "id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info("Sent the text" + text + " in Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
        except:
            self.log.error("Unable to sent the " + text + "in Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
            print_stack()
            assert False


    def getText(self, locatorValue, locatorType = "id"):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info("Got the text" + elementText + " from Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
        except:
            self.log.error("Unable to got the text " + elementText + "from Webelement with locator value" + locatorValue + "using locatorType" + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

        return elementText

    def isElementDisplayed(self, locatorValue, locatorType = "id"):
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info("Webelement is displayed with the locator value" + locatorValue + "using locatorType" + locatorType)
        except:
            self.log.error("Webelement is not displayed with the locator value" + locatorValue + "using locatorType" + locatorType)
            print_stack()
            assert False

        return elementDisplayed

    def scrollTo(self,locatorValue, locatorType = "id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info("Scrolled to WebElement with locator value" + locatorValue + "using locatorType" + locatorType)
        except:
            self.log.error("Unabled to scrolled to WebElement with locator value" + locatorValue + "using locatorType" + locatorType)
            print_stack()
            assert False

    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=AttachmentType.PNG)


    def dropDown(self, locatorValue,locatorType,visibleText):
        try:
            locatorType = locatorType.lower()
            ele = self.waitForElement(locatorValue, locatorType)
            options = Select(ele)
            options.select_by_visible_text(visibleText)
            self.log.info("Clicked on visible text" + visibleText + "in the drop down menu")
        except:
            self.log.error("Unable to Clicked on visible text"+ visibleText + "in the drop down menu")
            print_stack()
            assert False


    def setUserName(self, username): #"txt-username" , id
        self.driver.find_element(By.ID, "txt-username").clear()
        self.sendText(username,"txt-username","id")

        #self.driver.find_element(By.ID, "txt-username").send_keys(username)

    def setPassword(self, password): #"txt-password" , id
        self.driver.find_element(By.ID, "txt-password").clear()
        self.sendText(password, "txt-password", "id")

        #self.driver.find_element(By.ID, "txt-password").send_keys(password)