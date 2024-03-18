import pytest
import os
from selenium import webdriver
from env import result 



@pytest.fixture()
def driver():
    if(result['browser'] == "chrome"):
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(result['writeLoginUrl'])
    yield driver
    driver.close()