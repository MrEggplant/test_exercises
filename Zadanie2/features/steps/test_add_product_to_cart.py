import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when('I choose a product')
def choose_product(context):
    # IMPORTANT elements in this test has to be change, it's just for example
    button = context.driver.find_element(By.XPATH, '//*[@id="category-3"]/a')  # page "Clothes"
    button.click()
    button = context.driver.find_element(By.XPATH, '//ul[contains(@class, "category-sub-menu")]/li[1]/a')  # page "Men"
    button.click()
    product = context.driver.find_element(By.XPATH, '//*[contains(text(), "Hummingbird printed t-shirt")]')  # product
    product.click()


@when('I select color, size and quantity')
def select_details(context):
    detail = context.driver.find_element(By.XPATH, '//*[@value="11"]')  # color - black
    detail.click()
    detail = Select(context.driver.find_element(By.XPATH, '//*[@id="group_1"]'))  # size - M
    detail.select_by_visible_text('M')
    detail = context.driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]')  # quantity - 3
    detail.clear()
    detail.send_keys('3')


@when('I add product to cart')
def add_product_to_cart(context):
    context.driver.implicitly_wait(5)
    confirmation_button = context.driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary")]')
    confirmation_button.click()


@then('Confirmation popup is displayed')
def check_confirmation_popup(context):
    # we check by finding continue button on the popup
    continue_button = context.driver.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]')
    continue_button.is_displayed()


@then('Product with details are visible')
def check_product_details(context):
    context.driver.find_element(By.XPATH, '//button[contains(@class, "close")]/span').click()
    context.driver.find_element(By.XPATH, '// *[contains(text(), "shopping_cart")]').click()

    quantity = context.driver.find_element(By.XPATH, '//*[@value="3"]')
    quantity.is_displayed()
    lower_price = context.driver.find_element(By.XPATH, '// *[contains(@class, "product-line-info product-price h5 '
                                                        'has-discount")]')
    lower_price.is_displayed()
