from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class CommonAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    
    def wait_for(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def validate_the_title(self, titleText):
        self.wait.until(ec.title_is(titleText), 2000)

    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    
        