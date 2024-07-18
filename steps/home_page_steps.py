import time

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

@when('I click on the translation button on nav bar')
def step_impl(context):
    context.base.click_on(context.locators.HOME_PAGE_TRANSLATE_BUTTON)

@when('I select default language "{language}"')
def step_impl(context, language):
    context.base.click_on(context.locators.HOME_PAGE_DEFAULT_LANGUAGE_DROP)
    context.base.insert_text(context.locators.HOME_PAGE_DEFAULT_LANGUAGE_FIELD, language)
    context.home_page.default_language_select(language)

@when('I click reload page button')
def step_impl(context):
    context.base.click_on(context.locators.HOME_PAGE_LANGUAGE_RELOAD)
    time.sleep(0.5)


@then('The app language is switched to "{selected_language}"')
def step_impl(context, selected_language):
    context.home_page.language_check(selected_language, context.locators.HOME_PAGE_BANNER_TITLE)


