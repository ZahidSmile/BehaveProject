from behave import *
import time
from selenium.webdriver.common.by import By
import json

with open('D:\BehaveProject\cred.json') as f:
    data = json.load(f)


@given('Open Wallet Page & Authorize')
def openWallet(context):
    time.sleep(5)
    context.driver.get(data['wallet-url'])
    cookie = {'name': 'access_token', 'value': data['token']}
    context.driver.add_cookie(cookie)
    context.driver.get(data['wallet-url'])


@when('the user edit account details')
def editAccount(context):
    time.sleep(3)
    searchbar = context.driver.find_element(By.CSS_SELECTOR, ".wrap a")
    if searchbar.is_displayed():
        searchbar.click()
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '.withdra-btn').click()


@then('the user withdraw some amount')
def withdrawAmount(context):
    time.sleep(3)
    withdraw = context.driver.find_element(By.TAG_NAME, 'input')
    if withdraw.is_displayed():
        withdraw.click()
        time.sleep(2)
        withdraw.send_keys("200")
        context.driver.find_element(By.CSS_SELECTOR, '.withdra-btn').click()
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(1)').click()
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(1)').send_keys(data['pkcode'][0])
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(2)').send_keys(data['pkcode'][1])
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(3)').send_keys(data['pkcode'][2])
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(4)').send_keys(data['pkcode'][3])
        context.driver.find_element(By.CSS_SELECTOR, '.pincode-input-container input:nth-child(5)').send_keys(data['pkcode'][4])
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '#verify-btn').click()
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '.btn-wtdrw-now').click()
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '.share-wrap .wrap div:nth-child(2) a').click()
        time.sleep(3)
        context.driver.find_element(By.CSS_SELECTOR, '.btn-done').click()
        time.sleep(3)



