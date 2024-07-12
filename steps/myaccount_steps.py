from behave import *


@then('I am logged into the application')
def step_impl(context):
    context.myaccount_page.check_if_logged()
    context.base.click_on(context.locators.MY_ACCOUNT_USER_NAV_DROPDOWN)
    context.base.click_on(context.locators.MY_ACCOUNT_USER_NAV_DROPDOWN_LOGOUT)