import time
from browser import Browser
from selenium.webdriver.common.by import By

class Signup_Page(Browser):

    SIGNUP_PAGE_USERNAME_FIELD = (By.ID,'username')
    SIGNUP_PAGE_PASSWORD_FIELD = (By.ID, 'password')
    SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD = (By.ID, 'password_confirm')
    SIGNUP_PAGE_EMAIL_FIELD = (By.ID, 'email')
    SIGNUP_PAGE_SUBMIT_BUTTON = (By.ID,'sign_up_button')
    SIGNUP_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li')


    def check_signup_erros(self, error_message):
        is_error_message_correct = True

        error_list = self.driver.find_elements(*self.SIGNUP_ERRORS)
        for item in error_list:
            actual_err_text = item.text
            if error_message == actual_err_text:
                is_error_message_correct = True
                break
            else:
                is_error_message_correct = False


        assert is_error_message_correct








