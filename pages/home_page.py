from selenium.webdriver.common.by import By
from common_actions import CommonAction

class HomePage(CommonAction):

    FORM_ALERT = (By.ID, "flash")
    LOGOUT_BTN = (By.CLASS_NAME, "button")

    def check_login_logout_status(self):
        return self.wait_for(self.FORM_ALERT)
    
    def click_logout_button(self):
        self.find(self.LOGOUT_BTN).click()