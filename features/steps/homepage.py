from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@when('Search Field is Available')
def findSearch(context):
    time.sleep(5)
    status = context.driver.find_element(By.CSS_SELECTOR, "#searchKeywordText").is_displayed()
    assert status is True


@then('Search brand on it')
def searchBrand(context):
    search = context.driver.find_element(By.CSS_SELECTOR, "#searchKeywordText")
    search.click()
    search.send_keys("daraz")
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

