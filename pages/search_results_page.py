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

    def filter_option(self, locator, select_text): # not used right now, no element with <select> tag tested so far
        search_filter_bar = self.make_selector(locator)
        search_filter_bar.select_by_visible_text(select_text)

    def check_filter_result(self, locator, text):
        verified = False

        result_list = self.driver.find_elements(*locator)
        for item in result_list:
            if item.is_displayed():
                item_type = item.get_attribute('data-media-type')
            else:
                continue
            if item_type == text:
                verified = True

        assert verified






