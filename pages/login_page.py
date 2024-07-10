from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser


class Login_Page(Browser):

    USERNAME_FIELD = (By.XPATH,'//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH,'//input[@id="password"]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH,'//input[@id="login_button"]')
    ALL_LOGIN_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li[1]')
    OUT_OF_LOGIN_ATTEMPTS = (By.XPATH, '//h2[text()="Out of login attempts"]')

    def type_in_username(self,username):
        if username == "N/A":
            pass
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def type_in_password(self,password):
        if password == "N/A":
            pass
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()

    def check_login_error(self, error_message):
        actual_error_message = self.driver.find_element(*self.ALL_LOGIN_ERRORS).text
        assert actual_error_message == error_message, f'Expected error : {error_message}, Received error : {actual_error_message}'

    def deplete_login_attempts(self, username, password):
        wait = WebDriverWait(self.driver, 30)
        try:
            self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
            self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
            self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()
            wait.until(EC.presence_of_element_located(self.OUT_OF_LOGIN_ATTEMPTS))
        except TimeoutError:
            f'took to long'

    def check_if_blocked(self):
        verified = False
        if self.driver.title == 'Out of Login Attempts — The Movie Database (TMDB)':
            verified = True
        assert verified







