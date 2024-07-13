from behave import *



@when('I type valid username "{username}" and password "{password}" in corresponding input boxes on login page')
def step_impl(context, username, password):
    context.base.insert_text(context.locators.LOGIN_PAGE_USERNAME_FIELD, username)
    context.base.insert_text(context.locators.LOGIN_PAGE_PASSWORD_FIELD, password)

@when('I click the login button on login page')
def step_impl(context):
    context.base.click_on(context.locators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON)

@when('I type invalid username "{username}" and password "{password}" in corresponding input boxes on login page')
def step_impl(context,username,password):
    context.base.insert_text(context.locators.LOGIN_PAGE_USERNAME_FIELD, username)
    context.base.insert_text(context.locators.LOGIN_PAGE_PASSWORD_FIELD, password)

@then('I get an error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error(error_message)

@when('I try to log in more than ten times with invalid username "{username}"')
def step_impl(context,username):
    context.base.deplete_login_attempts(
        username,
        context.locators.LOGIN_PAGE_USERNAME_FIELD,
        context.locators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON,
        context.locators.LOGIN_PAGE_OUT_OF_LOGIN_ATTEMPTS
    )

@then("I am blocked from logging in again for 30 minutes")
def step_impl(context):
    context.login_page.check_if_blocked()



