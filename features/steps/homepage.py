from behave import *
import pathlib
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given('Launch chrome browser')
def launchBrowser(context):
    Chrome = pathlib.Path("C:\chromedriver\chromedriver.exe")
    if Chrome.exists():
        op = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(service=Service("C:\chromedriver\chromedriver.exe"), options=op)

@when('open savyour homepage')
def openHomePage(context):
    context.driver.maximize_window()
    context.driver.get("https://savyour.com.pk/")

@then('verify that logo is present on page')
def verifyLogo(context):
    time.sleep(5)
    status = context.driver.find_element(By.CSS_SELECTOR, ".desktop-logo").is_displayed()
    assert status is True

@then('close browser')
def step_impl(context):
    context.driver.close()

