from selenium.webdriver.common.by import By
from common_actions import CommonAction

class BingPage(CommonAction):
    BING_LOGO = By.ID('bLogo')
    BING_SEARCH_BAR = By.NAME('q')
    OWN_RESULT = By.XPATH('//*[@id="b_results"]/li[1]/div/div[1]')
    OWN_LINK_TEXT = By.LINK_TEXT('Own Company | Own Your Own Data')
    OWN_LOGO = By.XPATH('/html/body/section[1]/div[1]/div[1]/a')
    DROPDOWN_LIST = By.NAME('')

    def verify_bing_search_engine_title(self, titleText):
        self.validate_the_title(titleText)

    def validate_bing_logo_displayed(self):
        return self.is_element_displayed(self.BING_LOGO)
       
    def search_on_the_search_bar_and_hit_enter(self, inputText):
        self.wait_for(self.BING_SEARCH_BAR).send_keys(inputText)

    def click_on_the_fist_result(self):
        self.find(self.OWN_LINK_TEXT).click()

    def validate_own_image_displayed(self):
        return self.is_element_displayed(self.OWN_LOGO)

