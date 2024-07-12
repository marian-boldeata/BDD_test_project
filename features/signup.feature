Feature: Will test the account creation module of TMDB application


    @signup1
  Scenario Outline: Verify that anonymous user cannot create account with either invalid username, invalid email or invalid password
    Given I am on the TMDB home page
    When I click on Join TMDB button on navigation bar
    When I insert invalid set of information - "<username>", "<password>", "<conf_password>", "<email>"
    When I press the Sign Up button
    Then I receive an error message "<error_message>"
    Examples:
      | username   | email                   | password    | conf_password  | error_message                                                |
      | rando_nxme | m.boldeata@gmail.com    | 1234       | 1234            | Email has already been taken                                 |
      | mbx-bx     | randomm_email@random.com| 1234       | 1234            | Username has already been taken                              |
      | mbx-bx     | m.boldeatagmail.com     | 1234       | 1234            | Email does not appear to be valid                            |
      | rando_nxme | randomm_email@random.com| 123        | 123             | Password needs to be at least 4 characters long              |
      | rando_nxme | randomm_email@random.com| 1234       | abcd            | Password and password confirmation do not match              |
      | rando_&    | randomm_email@random.com| 1234       | 1234            | Username cannot contain ampersands                           |
      | rando_%    | randomm_email@random.com| 1234       | 1234            | Username cannot contain percentage signs                     |
      | rando_+    | randomm_email@random.com| 1234       | 1234            | Username cannot contain plus signs                           |
      | rando_/    | randomm_email@random.com| 1234       | 1234            | Username cannot contain slashes                              |

    @signup
  Scenario Outline: Verify that anonimous user cannot create account without providing either username, email or password
  Given I am on the TMDB home page
    When I click on Join TMDB button on navigation bar
    When I insert invalid set of information - "<username>", "<password>", "<conf_password>", "<email>"
    When I press the Sign Up button
    Then I receive an error message "<error_message>"
    Examples:
      | username    | email                      | password   |  conf_password  | error_message                                          |
      | N/A         | randomm_email@yahoo.com    | 1234       | 1234            | Username can't be blank                                |
      | rando_nxme  | N/A                        | 1234       | 1234            | Email can't be blank                                   |
      | rando_nxme  | randomm_email@yahoo.com    | 1234       | N/A             | Password confirm can't be blank                        |







      #need to implement error check in signup page, need good locator for errors - to be done

