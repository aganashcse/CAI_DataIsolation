
from Src.PageObject.Pages.LandingPage import LandingPage
from Src.TestBase.WebDriverSetup import WebDriverSetup

class TestLandingPage(WebDriverSetup):
    
    def test_title(self, loadDriver):
        landingPage = LandingPage(loadDriver)
        assert landingPage.title == loadDriver.title

    def test_logout_button(self, loadDriver):
        landingPage = LandingPage(loadDriver)
        landingPage.getlogout().is_displayed()