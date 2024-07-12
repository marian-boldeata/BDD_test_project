from selenium.webdriver.common.by import By

from browser import Browser


class Home_Page(Browser):

    LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT,'Login')
    JOIN_TMDB_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Join TMDB')

    def go_to_homepage(self):
        self.driver.get('https://www.themoviedb.org/')

