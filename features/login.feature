Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user navigates to the login page
    When the user enters valid username and password
    Then the user should be redirected to the dashboard