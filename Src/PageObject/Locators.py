

class LoginPageLocators:
    """ stores all elements css in Login Page """
    
    userName ="#username > input"
    password = "#password > input"
    loginButton = "#login > div > div > div.infaTileContent > div.form > div.submitBtn.loginBtn.ui-infa-button-emphasized > button > div > span"


class LandingPageLocators:
    """ stores all elements css in Landing Page """

    dataIntegreation = "#showProductsPage > div > div > div.products-container > div > div.my-products-container > div.product-table-window > div > div > div:nth-child(1) > div:nth-child(2) > a > div.product-btn-right-div > span"
    logout = "#showProductsPage > div > div > div.products-header > span.logout"


class DataIntegrationPageLocators:
    """ stores all elements css in Data Integration Page """

    logout = "#infaMenu2_2_a"
