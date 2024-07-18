Feature: Will validate translate function on main page nav bar

    @translate
  Scenario Outline: Verify that user can switch default language
    Given I am on the TMDB home page
    When I click on the translation button on nav bar
    When I select default language "<language>"
    When I click reload page button
    Then The app language is switched to "<selected_language>"

      Examples:
        |language   | selected_language  |
        |(de-DE)    | (de-DE)            |
        |(ro-RO)    | (ro-RO)            |
        |(es-ES)    | (es-ES)            |





