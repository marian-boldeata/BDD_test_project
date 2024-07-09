from behave import *

@when('I insert invalid set of information - "{username}", "{password}", "{conf_password}", "{email}"')
def step_impl(context,username, password, conf_password, email):
    context.signup_page.type_in_username(username)
    context.signup_page.type_in_password(password)
    context.signup_page.type_in_confirm_password(conf_password)
    context.signup_page.type_in_email(email)

@when('I press the Sign Up button')
def step_impl(context):
    context.signup_page.click_sign_up()

@then('I receive an error message "{error_message}"')
def step_impl(context, error_message):
    pass