from selenium.webdriver.common.by import By

from browser import Browser

class Myaccount_Page(Browser):

    USER_NAV_DROPDOWN = (By.XPATH,'//span[@class="avatar background_color pink"]')
    USER_NAV_DROPDOWN_LOGOUT = (By.LINK_TEXT,'Logout')


    def check_if_logged(self):
        assert self.driver.title == 'My Profile — The Movie Database (TMDB)'

