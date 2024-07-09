Feature: Will test the account creation module of TMDB application


    @sign
  Scenario Outline: Verify that anonymous user cannot create account without valid username,email and password
    Given I am on the TMDB home page
    When I click on Join TMDB button on navigation bar
    When I insert invalid set of information - "<username>", "<password>", "<conf_password>", "<email>"
    When I press the Sign Up button
    Then I receive an error message "<error_message>"
    Examples:
      | username   | email                  | password    | conf_password  | error_message                                                |
      | rando_nxme | m.boldeata@gmail.com   | 1234       | 1234            | Email has already been taken                                 |
      | mbx-bx     | random_email@random.com| 1234       | 1234            | Username has already been taken                              |
      | mbx-bx     | m.boldeatagmail.com    | 1234       | 1234            | Email does not appear to be valid                            |
      | rando_nxme | random_email@random.com| 123        | 123             | Password needs to be at least 4 characters long              |
      | rando_nxme | random_email@random.com| 1234       | 4321            | Password and password confirmation do not match              |

      #need work to ensure after pressing sign up, i get error messages rather than redirect to bullshit page - fixed using move_to_element from Action_Chains()
      #need to implement error check in signup page, need good locator for errors - to be done

