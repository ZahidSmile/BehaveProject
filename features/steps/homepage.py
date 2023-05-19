from behave import *
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

@given('Launch chrome browser')
def launchBrowser(context):
    Chrome = pathlib.Path("C:\chromedriver\chromedriver.exe")
    if Chrome.exists():
        op = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(service=Service("C:\chromedriver\chromedriver.exe"), options=op)

@when('open savyour homepage')
def openHomePage(context):
    context.driver.maximize_window()
    context.driver.get("https://staging.savyour.com.pk/")

@then('Login with session')
def step_impl(context):
    with open('D:\BehaveProject\\features\cred.json') as f:
        data = json.load(f)
    cookie = {'name': 'sut', 'value': data['session']}
    context.driver.add_cookie(cookie)
    context.driver.refresh()