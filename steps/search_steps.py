from behave import *

@when('I insert text "{text}" in search bar and click on search button')
def step_impl(context, text):
    context.base.insert_text(context.locators.HOME_PAGE_SEARCH_BAR, text)
    context.base.click_on(context.locators.HOME_PAGE_SEARCH_BUTTON)

@when('I am redirected to search results page with title "{search_term}"')
def step_impl(context, search_term):
    context.search_results_page.check_if_redirected(search_term)

@then('All search results contain text "{search_term}" in title')
def step_impl(context,search_term):
    context.search_results_page.check_search_results(search_term)
