from behave import *

@given('I am on the TMDB home page')
def step_impl(context):
    context.home_page.go_to_homepage()

@when('I click on the login button on the navigation bar')
def step_impl(context):
    context.base.click_on(context.locators.HOME_PAGE_LOGIN_BUTTON_NAV_BAR)

@when('I click on Join TMDB button on navigation bar')
def step_impl(context):
    context.base.click_on(context.locators.HOME_PAGE_JOIN_TMDB_BUTTON_NAV_BAR)