from selenium.webdriver.common.by import By
from common_actions import CommonAction

class LoginPage(CommonAction):

    FORM_AUTH_LOCATOR = (By.LINK_TEXT, "Form Authentication")
    FORM_USERNAME = (By.ID, "username")
    FORM_PASSWORD = (By.ID, "password")
    FORM_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")

    def navigate_to_form_page(self):
        self.wait_for(self.FORM_AUTH_LOCATOR).click()

    def enter_login_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.FORM_SUBMIT_BTN).click()
    