Feature: Will test search feature on home page
    @search
  Scenario: Verify that user can search using homepage search bar and validate results
    Given I am on the TMDB home page
    When I insert text "garfield" in search bar and click on search button
    When I am redirected to search results page with title "garfield"
    Then All search results contain text "garfield" in title

      """
      1. NEED TO FIX LOGIN ATTEMPTS IMPLEMENTATION
      2. Make up another scenario for search feature

      """