from behave import *


@then('I am logged into the application')
def step_impl(context):
    context.myaccount_page.check_if_logged()
    context.myaccount_page.logout()