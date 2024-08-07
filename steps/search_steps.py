from behave import *

@when('I insert text "{text}" in search bar and click on search button')
def step_impl(context, text):
    context.base.insert_text(context.home_page_locators.HOME_PAGE_SEARCH_BAR, text)
    context.base.click_on(context.home_page_locators.HOME_PAGE_SEARCH_BUTTON)

@when('I am redirected to search results page with title "{search_term}"')
def step_impl(context, search_term):
    context.search_results_page.check_if_redirected(search_term)

@then('All search results contain text "{search_term}" in title')
def step_impl(context,search_term):
    context.search_results_page.check_search_results(search_term, context.search_page_locators.SEARCH_RESULT_ITEM_TITLE)

@then('There are no search results on the search results page')
def step_impl(context):
    context.search_results_page.check_if_any_results(context.search_page_locators.SEARCH_PAGE_NO_S_RESULTS)

@when('I click on button Movies filter option')
def step_impl(context):
    context.base.click_on(context.search_page_locators.SEARCH_PAGE_MOVIE_FILTER)

@then('All search results are "{text}"')
def step_impl(context,text):
    context.search_results_page.check_filter_result(context.search_page_locators.SEARCH_PAGE_ITEM_DATA_TYPE, text)

@when('I click on People filter option')
def step_impl(context):
    context.base.click_on(context.search_page_locators.SEARCH_PAGE_PEOPLE_FILTER)

@when('I click on TV People filter option')
def step_impl(context):
    context.base.click_on(context.search_page_locators.SEARCH_PAGE_TV_SHOWS_FILTER)

@when('I click on Collections filter option')
def step_impl(context):
    context.base.click_on(context.search_page_locators.SEARCH_PAGE_COLLECTIONS_FILTER)
