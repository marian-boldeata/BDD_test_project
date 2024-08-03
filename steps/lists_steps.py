from behave import *


@when('I click on first search result title')
def step_impl(context):
    context.base.click_on(context.search_page_locators.SEARCH_RESULT_ITEM_TITLE)

@when('I click add to watchlist button')
def step_impl(context):
    context.base.click_on(context.item_details_page_locators.ITEM_DETAILS_PAGE_ADD_TO_WATCHLIST)

@then('User should see the movie added to watchlist on my account page')
def step_impl(context):
    item_name = context.show_details_page.store_added_item(context.item_details_page_locators.ITEM_DETAILS_PAGE_ITEM_TITLE)
    context.base.click_on(context.myaccount_page_locators.MY_ACCOUNT_USER_NAV_DROPDOWN)
    context.base.click_on(context.myaccount_page_locators.MY_ACCOUNT_USER_NAV_DROPDOWN_WATCHLIST)
    context.base.click_on(context.myaccount_page_locators.MY_ACCOUNT_USER_TOGGLE_MOVIES)
    context.myaccount_page.check_added_item(item_name, context.myaccount_page_locators.MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE)


@given('I am on the TMDB my account page')
def step_impl(context):
    context.myaccount_page.go_to_myaccount_page()

@when('I hover over watchlist button on shortcut bar and click movies')
def step_impl(context):
    context.base.hover_over_click_chain(locator=context.myaccount_page_locators.MY_ACCOUNT_USER_SHORTCUTBAR_WATCHLIST_DROPDOWN,
                                        locator1=context.myaccount_page_locators.MY_ACCOUNT_USER_SHORTCUTBAR_WATCHLIST_MOVIES)


@when('I click the remove button inside the movie card')
def step_impl(context):
    context.base.click_on(context.myaccount_page_locators.MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE_REMOVE)

@when('I click on favourite button inside the movie card')
def step_impl(context):
    context.base.click_on(context.myaccount_page_locators.MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE_ADD_TO_FAV)

@then('The movie card is removed from my watchlist')
def step_impl(context):
    context.myaccount_page.check_if_removed(context.myaccount_page_locators.MY_ACCOUNT_USER_WATCHLIST_MOVIE_CARD)

@then('The movide should be added to favourites list')
def step_impl(context):
    item_name = context.show_details_page.store_added_item(context.myaccount_page_locators.MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE)
    context.base.hover_over_click_chain(locator=context.myaccount_page_locators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_DROPDOWN,
                                        locator1=context.myaccount_page_locators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_DROPDOWN,
                                        locator2=context.myaccount_page_locators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_MOVIES_DROPDOWN)
    context.myaccount_page.check_added_item(item_name, context.myaccount_page_locators.MY_ACCOUNT_USER_OVERVIEW_FAVOURITES_FIRST_TITLE)
