Feature: Will test the filter options available on search results page

  Background:
    Given I am on the TMDB home page
    When I insert text "garfield" in search bar and click on search button
    When I am redirected to search results page with title "garfield"
@movie
Scenario: Filter search results by Movies
    When I click on button Movies filter option
    Then All search results are "movie"
@movie
Scenario: Filter search results by People
    When I click on People filter option
    Then All search results are "person"
@movie
Scenario: Filter search results by TV Shows
    When I click on TV People filter option
    Then All search results are "tv"
@movie
Scenario: Filter search results by Collections
    When I click on Collections filter option
    Then All search results are "collection"