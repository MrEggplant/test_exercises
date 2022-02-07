Feature: As I new user I want to registrate to webpage

  Background:
    Given I am on main page
    And I am not login

  Scenario: New user registrate himself
    When I click a login button
    And I click registration link
    And I type user data correctly
    Then User is created and name is visible