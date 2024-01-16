from behave import *
from selenium.webdriver.common.by import By
import time


@given('Instore Banner Available')
def findInstore(context):
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, 'a [title="Go To Instore"]').click()
    time.sleep(1)
    listing = context.driver.find_elements(By.CSS_SELECTOR, '.in-store-listing h3')
    for l in listing:
        time.sleep(2)
        if l.is_displayed():
            context.driver.back()
            break

@when('the user navigates to the Home Page')
def checkHomepageSections(context):
    one = 1
    time.sleep(2)
    heading = context.driver.find_element(By.CSS_SELECTOR, ".container h2")
    if heading.is_displayed():
        headings = context.driver.find_elements(By.CSS_SELECTOR, ".container h2")
        for title in headings:
            print("Heading Number " + str(one) + " " + title.text)
            one = one + 1

@then('the user checks the visibility of all sections')
def checkSectionsSeeAll(context):
    SeeAll = context.driver.find_elements(By.CSS_SELECTOR, 'div.container a.text-danger[href]')
    for link in SeeAll:
        if link.is_displayed():
            print(link.get_attribute('href'))
            URL = link.get_attribute('href')
            time.sleep(1)
            context.driver.execute_script("window.open()")
            print("Window Open")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            print("Tab Switched")
            time.sleep(1)
            context.driver.get(URL)
            print("Link Opened")
            time.sleep(1)
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            print("Tab Switch to Home")
