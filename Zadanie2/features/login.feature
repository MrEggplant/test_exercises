Feature: As a User I want to login to webpage

  Background:
    Given I am on main page
    And I am not login

  Scenario: User login to website
    When I click login button
    And I type login and password
    And I click submit button
    Then User will be login

  Scenario Outline: Login with incorrect data
    When I click login button
    And I type <email> and <password>
    And I click submit button
    Then User will not login
    Examples:
    |email|password|
    |bozena+1@aa.aa|aAAAAAA|
    |aa@bb.aa|30zeNA!|
