
import pytest
import pdb

from Src.PageObject.Pages.LoginPage import LoginPage
from Src.TestBase.WebDriverSetup import WebDriverSetup


# @pytest.fixture(scope="package")
# def loadDriver():
#     webDriver = WebDriverSetup()
#     driver = webDriver.driver
#     properties = webDriver.properties
#     driver.maximize_window()
#     driver.get(properties.get("ApplicationProperties", "URL"))
#     loginPage = LoginPage(driver)
#     return loginPage.login(user={"userName":properties.get("ApplicationProperties", \
#         "userName"), "password":properties.get("ApplicationProperties", "password")})

if __name__=="__main__":
    import Scripts.test_LandingPage