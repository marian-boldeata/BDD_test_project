from behave import *



@when('I type valid username "{username}" and password "{password}" in corresponding input boxes on login page')
def step_impl(context, username, password):
    context.login_page.type_in_username(username)
    context.login_page.type_in_password(password)

@when('I click the login button on login page')
def step_impl(context):
    context.login_page.click_login_button()

@when('I type invalid username "{username}" and password "{password}" in corresponding input boxes on login page')
def step_impl(context,username,password):
    context.login_page.type_in_username(username)
    context.login_page.type_in_password(password)

@then('I get an error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error(error_message)



