Feature: Conference Login
  Scenario: Login to Larvol Conference with valid parameters
    Given I Launch chrome browser
    When I Open conference login page
    And Enter username "Sagar@simformsolutions.com" and password "Sagar@123"
    And Click on Login button
    Then User must successfully login to dashboard page


  Scenario Outline: Login to Larvol Conference with valid parameters
    Given I Launch chrome browser
    When I Open conference login page
    And Enter username "<username>" and password "<password>"
    And Click on Login button
    Then User must successfully login to dashboard page

    Examples:
      | username                   | password  |
      | sagar@simform.com          | Sagar     |
      | sagar@gmail.com            | 123456    |
      | mayuri@simform.com         | mayu@123  |
      | sagar@simformsolutions.com | Sagar@123 |
      | saga123@hh.com             | 1233333   |