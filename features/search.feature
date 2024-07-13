Feature: Will test search feature on home page
    @search
  Scenario: Verify that user can search using homepage search bar and validate results
    Given I am on the TMDB home page
    When I insert text "garfield" in search bar and click on search button
    When I am redirected to search results page with title "garfield"
    Then All search results contain text "garfield" in title

    @search
  Scenario: Verify that application will not return search results if none match
    Given I am on the TMDB home page
    When I insert text "asdasd" in search bar and click on search button
    When I am redirected to search results page with title "asdasd"
    Then There are no search results on the search results page




