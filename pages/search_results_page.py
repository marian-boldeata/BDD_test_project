from selenium.webdriver.common.by import By

from browser import Browser

class Search_Results_Page(Browser):


    def check_if_redirected(self, search_term):
        if search_term in self.driver.title:
            assert True

    def check_search_results(self, search_term, locator):
        validated = False
        result_items = self.driver.find_elements(*locator)
        result_titles_text = []
        for item in result_items:
            if item.is_displayed():
                movie_title = item.text
                result_titles_text.append(movie_title.lower())
        for i in range(len(result_titles_text)):
            if search_term in result_titles_text[i]:
                validated = True

        assert validated

    def check_if_any_results(self, locator):
        validated = False
        if self.driver.find_element(*locator).is_displayed():
            validated = True
        assert validated

