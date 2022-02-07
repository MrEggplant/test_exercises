Feature: As a User I want to add products to the cart

    Background:
    Given I am on main page
    When I click login button
    And I type login and password

    Scenario: Add product to the cart
      When I choose a product
      And I select color, size and quantity
      And I add product to cart
      Then Confirmation popup is displayed
      And Product with details are visible
