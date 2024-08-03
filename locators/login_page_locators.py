from selenium.webdriver.common.by import By


class Login_page_locators():
    LOGIN_PAGE_USERNAME_FIELD = (By.ID, "username")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_PAGE_SUBMIT_LOGIN_BUTTON = (By.ID, "login_button")
    LOGIN_PAGE_OUT_OF_LOGIN_ATTEMPTS = (By.XPATH, '//h2[text()="Out of login attempts"]')