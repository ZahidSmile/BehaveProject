from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Search Field is Available')
def findSearch(context):
    time.sleep(5)
    status = context.driver.find_element(By.CSS_SELECTOR, "#searchKeywordText").is_displayed()
    assert status is True


@when('Search brand on it')
def searchBrand(context):
    searchbar = context.driver.find_element(By.CSS_SELECTOR, "#searchKeywordText")
    if searchbar.is_displayed():
        searchbar.click()
        brand = "Ideas"
        searchbar.send_keys(brand)
        searchbar.send_keys(Keys.RETURN)
        time.sleep(3)


@then('open brand')
def openBrand(context):
    brands = context.driver.find_elements(By.CSS_SELECTOR, 'app-brand-profile-cards a h3')
    for brand in brands:
        if brand.is_displayed() and brand.text == "Ideas":
            brand.click()
            print("Ideas Brand Found & Clicked")
            print(" ")
            break

