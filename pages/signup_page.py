import time
from browser import Browser
from selenium.webdriver.common.by import By

class Signup_Page(Browser):

    SIGNUP_USERNAME_FIELD = (By.ID,'username')
    SIGNUP_PASSWORD_FIELD = (By.ID, 'password')
    SIGNUP_PASSWORD_CONFIRM_FIELD = (By.ID, 'password_confirm')
    SIGNUP_EMAIL_FIELD = (By.ID, 'email')
    SIGNUP_BUTTON = (By.ID,'sign_up_button')
    SIGNUP_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li')

    def type_in_username(self, username):
        if username == "N/A":
            pass
        else:
            self.driver.find_element(*self.SIGNUP_USERNAME_FIELD).send_keys(username)

    def type_in_password(self,password):
        if password == "N/A":
            pass
        else:
            self.driver.find_element(*self.SIGNUP_PASSWORD_FIELD).send_keys(password)

    def type_in_confirm_password(self,conf_password):
        if conf_password == "N/A":
            pass
        else:
            self.driver.find_element(*self.SIGNUP_PASSWORD_CONFIRM_FIELD).send_keys(conf_password)

    def type_in_email(self,email):
        if email == "N/A":
            pass
        else:
            self.driver.find_element(*self.SIGNUP_EMAIL_FIELD).send_keys(email)

    def click_sign_up(self):
        signupbtn = self.driver.find_element(*self.SIGNUP_BUTTON)
        self.action.move_to_element(signupbtn).perform()
        time.sleep(0.5)
        self.action.move_to_element(signupbtn).click().perform()

    def check_sigunp_erros(self, error_message):
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








