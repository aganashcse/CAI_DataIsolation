from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Src.PageObject.Locators import LandingPageLocators

class LandingPage:

    def __init__(self, webDriver) -> None:
        self.driver = webDriver
        self.title = "Informatica Cloud"
        self.logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, \
                LandingPageLocators.logout)))


    def getlogout(self):
        return self.logout