"""
File contains all locators with name format - name_of_page + description_of_locator

"""
from selenium.webdriver.common.by import By


class Locators:

    "HOME PAGE LOCATORS"
    HOME_PAGE_LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Login')
    HOME_PAGE_JOIN_TMDB_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Join TMDB')
    HOME_PAGE_SEARCH_BAR = (By.ID,'inner_search_v4')
    HOME_PAGE_SEARCH_BUTTON = (By.XPATH,'//input[@value="Search"]')


    "LOGIN PAGE LOCATORS"
    LOGIN_PAGE_USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    LOGIN_PAGE_PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_PAGE_SUBMIT_LOGIN_BUTTON = (By.XPATH, '//input[@id="login_button"]')

    "SIGNUP PAGE LOCATORS"
    SIGNUP_PAGE_USERNAME_FIELD = (By.ID, 'username')
    SIGNUP_PAGE_PASSWORD_FIELD = (By.ID, 'password')
    SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD = (By.ID, 'password_confirm')
    SIGNUP_PAGE_EMAIL_FIELD = (By.ID, 'email')
    SIGNUP_PAGE_SUBMIT_BUTTON = (By.ID, 'sign_up_button')

    "MY ACCOUNT PAGE LOCATORS"
    MY_ACCOUNT_USER_NAV_DROPDOWN = (By.XPATH, '//span[@class="avatar background_color pink"]')
    MY_ACCOUNT_USER_NAV_DROPDOWN_LOGOUT = (By.LINK_TEXT, 'Logout')

    "SEARCH PAGE LOCATORS"
