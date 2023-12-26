from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


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

#
# @then('Check Instore Data')
# def checkInstore(context):
#     time.sleep(1)
#     # pages = context.driver.find_element(By.CSS_SELECTOR, '.pagination-next')
#     # context.driver.execute_script("return arguments[0].scrollIntoView(true);", pages)
#     context.send_keys(Keys.END)


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


# @given('Bachat Deals Section Visible')
# def checkBachatDeal(context):
#     one = 0
#     elem = context.driver.find_elements(By.CSS_SELECTOR, 'div.row .swiper-wrapper a.cursor-pointer')
#     for deals in elem:
#         if deals.is_displayed():
#             time.sleep(1)
#             context.driver.find_elements(By.CSS_SELECTOR,'div.row .swiper-wrapper a.share-it')[one].click()
#             time.sleep(1)
#             context.driver.find_elements(By.CSS_SELECTOR,'div.row .swiper-wrapper a.share-it')[one].click()
#             one = one + 1
#
#
# @given('Trending Brand Section Visible')
# def checkTrendingBrands(context):
#     print("Trending Brands")
#     time.sleep(2)
#
#     # To Scroll on a specific Class We Use Element
#     element = context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-white')
#     context.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
#     # Scroll End
#
#     time.sleep(2)
#     elem = context.driver.find_element(By.CSS_SELECTOR, 'div.left a')
#     if elem.is_displayed():
#         URL = elem.get_attribute('href')
#         print(URL)
#         context.driver.execute_script("window.open()")
#         time.sleep(1)
#         context.driver.switch_to.window(context.driver.window_handles[1])
#         print("Tab Switched")
#         time.sleep(1)
#         context.driver.get(URL)
#         print("Link Opened")
#         time.sleep(1)
#         context.driver.close()
#         context.driver.switch_to.window(context.driver.window_handles[0])
#