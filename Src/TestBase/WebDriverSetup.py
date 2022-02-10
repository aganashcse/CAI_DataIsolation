
import pytest
from selenium import webdriver
from Src.PageObject.Pages.LoginPage import LoginPage

from Src.TestBase.utility import Utility


CONSTANTS = {
    "propertyFile" : "properties.ini"
}
properties = {}

class WebDriverSetup:
    @pytest.fixture(scope="package")
    def driver(self):
        global properties
        properties = Utility.loadPropertiesFile(CONSTANTS.get("propertyFile"))
        # driver = webdriver.Chrome(properties.get("SystemProperties", "chromeDriverPath"))
        driver = webdriver.Chrome("C:/Users/ganbu/Desktop/Workspace/Dependancies/chromedriver.exe")
        yield driver
        driver.quit()

    @pytest.fixture(scope="package")
    def loadDriver(self, driver):
        driver.maximize_window()
        driver.get("https://qa-ma.patch.infaqa.com/identity-service/home")
        loginPage = LoginPage(driver)
        loginPage.login(user={"userName":"Patchenv_BS", "password":"Password123"})
        return driver