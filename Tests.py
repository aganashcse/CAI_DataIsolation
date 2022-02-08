from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import pdb

from utility import Utility

CONSTANTS = {
    "propertyFile" : "properties.ini"
}

properties = {}

def LoginPage(driver, user):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForLogin",\
             "userName")))).send_keys(user.get("userName"))
    driver.find_element_by_css_selector(properties.get("WebElementCssForLogin", "password"))\
        .send_keys(user.get("password"))
    driver.find_element_by_css_selector(properties.get("WebElementCssForLogin", "loginButton"\
        )).click()
    return driver

@pytest.fixture(scope="module")
def driver():
    global properties
    properties = Utility.loadJsonFile(CONSTANTS.get("propertyFile"))
    driver = webdriver.Chrome(properties.get("SystemProperties", "chromeDriverPath"))
    # driver.get(properties.get("ApplicationProperties", "URL"))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver):
    driver.get(properties.get("ApplicationProperties", "URL"))
    driver.maximize_window()
    return LoginPage(driver, user={"userName":properties.get("ApplicationProperties", \
        "userName"), "password":properties.get("ApplicationProperties", "password")})


class TestLandingPage:

    def test_title(self, login):
        title = "Informatica Cloud"
        assert title == login.title
        # pdb.set_trace()

    def test_logout_button(self, login):
        # pdb.set_trace()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForLandinPage","logout")))).is_displayed()

class TestDataIntegrationPage:
    @pytest.fixture(scope="class", autouse=True)
    def navigate_to_data_integration(self, login):
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForLandinPage","dataIntegreation")))).click()
        return login

    def test_title(self, navigate_to_data_integration):
        title = "Informatica Cloud"
        assert title == navigate_to_data_integration.title

    def test_logout_button(self, navigate_to_data_integration):
        # pdb.set_trace()
        WebDriverWait(navigate_to_data_integration, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForDataIntegrationPage","logout")))).is_displayed()