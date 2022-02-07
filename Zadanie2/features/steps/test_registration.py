import time
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@given('I am on main page')
def open_page(context):
    context.driver = webdriver.Chrome('/Users/emil-mac/Downloads/chromedriver')
    context.driver.implicitly_wait(5)
    context.driver.get('https://autodemo.testoneo.com/pl/')


@given('I am not login')
def check_login_user(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Zaloguj się")]').is_displayed()


@when('I click a login button')
def click_login_button(context):
    button = context.driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]')
    button.click()
    context.driver.find_element(By.LINK_TEXT, 'Nie masz konta? Załóż je tutaj').is_displayed()


@when('I click registration link')
def click_registration_link(context):
    button = context.driver.find_element(By.XPATH, '/html/body/main/section/div/div/section/section/div/a')
    button.click()
    context.driver.find_element(By.NAME, 'id_customer').is_displayed()


@when('I type user data correctly')
def type_user_data(context):
    name_field = context.driver.find_element(By.XPATH, '//input[@name="firstname"]')
    name_field.send_keys('Bozena')
    surname_field = context.driver.find_element(By.XPATH, '//input[@name="lastname"]')
    surname_field.send_keys('Kowalska')
    email_field = context.driver.find_element(By.XPATH, '//input[@name="email"]')
    email = 'bozena+' + str(time.time()) + '@aa.aa'
    email_field.send_keys(email)
    email_field = context.driver.find_element(By.XPATH, '//input[@name="password"]')
    email_field.send_keys('30zeNA!')
    submit_button = context.driver.find_element(By.XPATH, '//button[contains(@class, "form-control-submit")]')
    submit_button.click()


@then('User is created and name is visible')
def check_login_user(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Bozena Kowalska")]').is_displayed()
