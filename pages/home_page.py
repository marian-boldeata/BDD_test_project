
from browser import Browser


class Home_Page(Browser):


    def go_to_homepage(self):
        self.driver.get('https://www.themoviedb.org/')

