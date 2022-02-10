
class TestDataIntegrationPage:
    @pytest.fixture(scope="class", autouse=True)
    def navigate_to_data_integration(self, loadDriver):
        WebDriverWait(loadDriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForLandinPage","dataIntegreation")))).click()
        return loadDriver

    def test_title(self, navigate_to_data_integration):
        title = "Informatica Cloud"
        assert title == navigate_to_data_integration.title

    def test_logout_button(self, navigate_to_data_integration):
        # pdb.set_trace()
        WebDriverWait(navigate_to_data_integration, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, properties.get("WebElementCssForDataIntegrationPage","logout")))).is_displayed()
