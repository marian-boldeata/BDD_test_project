Feature: Will test the login module of TMDB application

  # valid credentials - username mbx-bx // password 4231

  Scenario: Verify that user can successfully log in with valid username and password
    Given I am on the TMDB home page
    When I click on the login button on the navigation bar
    When I type valid username "mbx-bx" and password "4231" in corresponding input boxes on login page
    When I click the login button on login page
    Then I am logged into the application


  Scenario Outline: Verify that user cannot log in with invalid username and password
    Given I am on the TMDB home page
    When I click on the login button on the navigation bar
    When I type invalid username "<username>" and password "<password>" in corresponding input boxes on login page
    When I click the login button on login page
    Then I get an error message "<error_message>"
    Examples:
      | username       | password | error_message                                            |
      | testname_      |12345     | We couldn't find your username.                          |
      | mbx-bx         |N/A       | We couldn't validate your information. Want to try again?|
      | N/A            |123123    | We couldn't find your username.                          |

  Scenario: Verify that user will be blocked from trying to log in after 10 failed attempts
    Given I am on the TMDB home page
    When I click on the login button on the navigation bar
    When I try to log in more than ten times with invalid username "testname_"
    Then I am blocked from logging in again for 30 minutes




