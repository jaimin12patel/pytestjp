from pages.bing_page import BingPage

import sys
sys.path.append('/Users/jaiminpatel/Documents/Automation/pytestjp')

def test_form_authentication(driver):
    bingPage = BingPage(driver)

    bingPage.verify_bing_search_engine_title('bing')

    assert bingPage.validate_bing_logo_displayed() is True
    
    bingPage.search_on_the_search_bar_and_hit_enter('owndata')

    bingPage.click_on_the_fist_result()

    assert bingPage.validate_own_image_displayed() is True

