from selenium.webdriver.common.by import By


from browser import Browser


class Login_Page(Browser):


    ALL_LOGIN_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li[1]')

    def login_user(self):
        self.driver.get('https://www.themoviedb.org/login')
        self.driver.find_element(By.ID, "username").send_keys("mbx-bx")
        self.driver.find_element(By.ID,"password").send_keys("4231")
        self.driver.find_element(By.ID, "login_button").click()



    def check_login_error(self, error_message):
        actual_error_message = self.driver.find_element(*self.ALL_LOGIN_ERRORS).text
        assert actual_error_message == error_message, f'Expected error : {error_message}, Received error : {actual_error_message}'


    def check_if_blocked(self):
        verified = False
        if self.driver.title == 'Out of Login Attempts — The Movie Database (TMDB)':
            verified = True
        assert verified








