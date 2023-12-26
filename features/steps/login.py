from behave import *
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

with open('D:\BehaveProject\cred.json') as f:
    data = json.load(f)

@given('the user launches the Chrome browser')
def before_all(context):
    Chrome = pathlib.Path("C:\chromedriver\chromedriver.exe")
    if Chrome.exists():
        op = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(service=Service("C:\chromedriver\chromedriver.exe"), options=op)


@when('the user opens the Savyour website')
def openHomePage(context):
    context.driver.maximize_window()
    context.driver.get(data['pkurl'])


@then('the user logs in with phone number')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '.non-auth-section .Continue-with-Phone-Number').click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '#otp-number').click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '.countryPhoneNumber').send_keys(data['pkphone'])
    context.driver.find_element(By.CSS_SELECTOR, '#loginOTP').click()
    time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-1').click()
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-1').send_keys(data['pkcode'][0])
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-2').send_keys(data['pkcode'][1])
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-3').send_keys(data['pkcode'][2])
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-4').send_keys(data['pkcode'][3])
    context.driver.find_element(By.CSS_SELECTOR, '.otpCode-5').send_keys(data['pkcode'][4])
    context.driver.find_element(By.CSS_SELECTOR, '.verifyOTP').click()
    time.sleep(2)
