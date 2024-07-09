from behave import *

@given('I am on the TMDB home page')
def step_impl(context):
    context.home_page.go_to_homepage()

@when('I click on the login button on the navigation bar')
def step_impl(context):
    context.home_page.click_login_button()

@when('I click on Join TMDB button on navigation bar')
def step_impl(context):
    context.home_page.click_JOIN_TMDB_button()