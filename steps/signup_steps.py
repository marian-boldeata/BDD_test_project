from behave import *

@when('I insert invalid set of information - "{username}", "{password}", "{conf_password}", "{email}"')
def step_impl(context,username, password, conf_password, email):
    context.base.insert_text(context.signup_page_locators.SIGNUP_PAGE_USERNAME_FIELD, username)
    context.base.insert_text(context.signup_page_locators.SIGNUP_PAGE_PASSWORD_FIELD, password)
    context.base.insert_text(context.signup_page_locators.SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD, conf_password)
    context.base.insert_text(context.signup_page_locators.SIGNUP_PAGE_EMAIL_FIELD, email)

@when('I press the Sign Up button')
def step_impl(context):
    context.base.click_hold(context.signup_page_locators.SIGNUP_PAGE_SUBMIT_BUTTON)

@then('I receive an error message "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_signup_erros(error_message)