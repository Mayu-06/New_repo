from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@given('I Launch browser')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)
    context.driver.maximize_window()


@when('I Open conference application')
def step_impl(context):
    context.driver.get('https://confstage.larvol.com/conference')


@when('Enter valid username "{user}" and valid password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH, '//input[@type = "email"]').send_keys(user)
    context.driver.find_element(By.XPATH, '//input[@type = "password"]').send_keys(pwd)


@when('Click on Login')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@class = "btn btn-purple btn-block btn-lg"]').click()


@then('User must login to the dashboard page')
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


@when('Click on any Conference')
def step_impl(context):
    time.sleep(10)
    element = context.driver.find_element(By.XPATH, "//div[normalize-space()='EULAR 2022']")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    context.driver.find_element(By.XPATH, "//div[normalize-space()='EULAR 2022']").click()


@then('Conference page should display')
def step_impl(context):
    time.sleep(10)
    try:
        text1 = context.driver.find_element(By.XPATH, "//div[@class='conference-title']").text
    except:
        context.driver.close()
        assert False, 'Test Failed'
    if text1 == 'Annual Congress of European League Against Rheumatism':
        context.driver.close()
        assert True, "Test Passed"


@then('Click on starred abstract page')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH,"//a[normalize-space()='Starred Abstracts']").click()
    context.driver.close()
