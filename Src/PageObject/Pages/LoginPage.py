
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Src.PageObject.Locators import LoginPageLocators
class LoginPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.userName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageLocators.userName)))
        self.password = driver.find_element_by_css_selector(LoginPageLocators.password)
        self.loginBtn = driver.find_element_by_css_selector(LoginPageLocators.loginButton)

    def login(self, user):
        self.userName.send_keys(user.get("userName"))
        self.password.send_keys(user.get("password"))
        self.loginBtn.click()