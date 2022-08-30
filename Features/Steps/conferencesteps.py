from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('Open conference login page')
def open_login_page(context):
    context.driver.get('https://confstage.larvol.com/conference')


@then('Verify that logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//img[@alt='Larvol Conference']").is_displayed()
    assert status is True


@then('Close browser')
def close_browser(context):
    context.driver.close()
