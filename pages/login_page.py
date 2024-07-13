from selenium.webdriver.common.by import By


from browser import Browser


class Login_Page(Browser):


    ALL_LOGIN_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li[1]')



    def check_login_error(self, error_message):
        actual_error_message = self.driver.find_element(*self.ALL_LOGIN_ERRORS).text
        assert actual_error_message == error_message, f'Expected error : {error_message}, Received error : {actual_error_message}'


    def check_if_blocked(self):
        verified = False
        if self.driver.title == 'Out of Login Attempts — The Movie Database (TMDB)':
            verified = True
        assert verified

"""
        try:
            self.insert_text(user_field, username)
            self.insert_text(pass_field,password)
            self.click_on(sign_btn)
            wait.until(EC.presence_of_element_located(expected_element))
        except TimeoutError:
            f'took to long'
"""






