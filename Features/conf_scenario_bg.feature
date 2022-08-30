Feature: Conference Login

  Background: common steps
    Given I Launch browser
    When I Open conference application
    And Enter valid username "Sagar@simformsolutions.com" and valid password "Sagar@123"
    And Click on Login

  Scenario: Login to Larvol Conference
    Then User must login to the dashboard page

  Scenario: Open any conference
    When Click on any Conference
    Then Conference page should display


  Scenario: Click on starred abstract page
    When Click on any Conference
    Then Click on starred abstract page
