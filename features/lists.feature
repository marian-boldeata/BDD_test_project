Feature: Will test functionality of watchlist and list features


    @list @registered_user
    Scenario: Will test if logged in user can add a movie to watchlist
      Given I am on the TMDB home page
      When I insert text "ethernal city" in search bar and click on search button
      When I click on button Movies filter option
      When I click on first search result title
      When I click add to watchlist button
      Then User should see the movie added to watchlist on my account page

    @list
    Scenario: Test functionality of add to favorites button from watchlist
      Given I am on the TMDB my account page
      When I hover over watchlist button on shortcut bar and click movies
      When I click on favourite button inside the movie card
      Then The movide should be added to favourites list


    @list
    Scenario: Test functionality of Remove button from watchlist
      Given I am on the TMDB my account page
      When I hover over watchlist button on shortcut bar and click movies
      When I click the remove button inside the movie card
      Then The movie card is removed from my watchlist

      """





      report bugs in jira
      """

      # also, change login feature verification using below instruction

     """Dictionar care sa contina chei cu numele campurilor din formular si valoarea cheilor sa reprezinte eroarea care ar trebui sa apara pe campul respectiv

      In functia de verificare mesaje sa se extraga toate mesajele din browser intr-o lista.

      Lista se va parcurge concomitent cu dictionarul si se va verifica daca eroarea de pe valoarea din dictionar este egala cu eroarea extrasa dinamic din browser"""
