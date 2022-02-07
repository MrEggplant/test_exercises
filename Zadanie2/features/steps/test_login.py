from behave import *
from selenium.webdriver.common.by import By


@when('I click login button')
def click_login_button(context):
    button = context.driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]')
    button.click()
    context.driver.find_element(By.LINK_TEXT, 'Nie masz konta? Załóż je tutaj').is_displayed()


@when('I type login and password')
def type_login_password(context):
    email_field = context.driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[1]/div[1]/input')
    email = 'bozena+1@aa.aa'
    email_field.send_keys(email)
    email_field = context.driver.find_element(By.XPATH, '//input[@name="password"]')
    email_field.send_keys('30zeNA!')


@when('I click submit button')
def click_submit(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit-login"]').click()


@then('User will be login')
def check_login_user(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Bozena Kowalska")]').is_displayed()


@when('I type {email} and {password}')
def type_incorrect_email_password(context, email, password):
    email_field = context.driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[1]/div[1]/input')
    email_field.send_keys(email)
    password_field = context.driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys(password)


@then('User will not login')
def check_wrong_login_data_message(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Błąd uwierzytelniania.")]').is_displayed()
