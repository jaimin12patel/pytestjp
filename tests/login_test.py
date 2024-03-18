from pages.login_page import LoginPage
from pages.home_page import HomePage
import sys
sys.path.append('/Users/jaiminpatel/Documents/Automation/pytestjp')

def test_form_authentication(driver):
    loginPage = LoginPage(driver)
    homePage = HomePage(driver)

    loginPage.navigate_to_form_page()
    loginPage.enter_login_username("tomsmith")
    loginPage.enter_login_password("SuperSecretPassword!")
    loginPage.click_login_button()

    assert "logged in" in homePage.check_login_logout_status().text 

    homePage.click_logout_button()
    assert "logged out" in homePage.check_login_logout_status().text