import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('I Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('I Open conference login page')
def step_impl(context):
    context.driver.get('https://confstage.larvol.com/conference')


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, '//input[@type = "email"]').send_keys(user)
    context.driver.find_element(By.XPATH, '//input[@type = "password"]').send_keys(pwd)


@when('Click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@class = "btn btn-purple btn-block btn-lg"]').click()


@then('User must successfully login to dashboard page')
def step_impl(context):
    time.sleep(10)
    try:
        text1 = context.driver.find_element(By.XPATH, "//span[contains(text(),'Purchased Conferences')]").text
    except:
        context.driver.close()
        assert False, 'Test Failed'
    if text1 == 'Purchased Conferences':
        context.driver.close()
        assert True, "Test Passed"
