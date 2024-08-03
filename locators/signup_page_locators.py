from selenium.webdriver.common.by import By


class Signup_page_locators():

    SIGNUP_PAGE_USERNAME_FIELD = (By.ID, 'username')
    SIGNUP_PAGE_PASSWORD_FIELD = (By.ID, 'password')
    SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD = (By.ID, 'password_confirm')
    SIGNUP_PAGE_EMAIL_FIELD = (By.ID, 'email')
    SIGNUP_PAGE_SUBMIT_BUTTON = (By.ID, 'sign_up_button')