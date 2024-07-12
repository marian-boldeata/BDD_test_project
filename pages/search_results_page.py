from selenium.webdriver.common.by import By

from browser import Browser

class Search_Results_Page(Browser):
    SEARCH_RESULT_ITEM_TITLE = (By.XPATH, '//div[@class="content_wrapper"]//div[@class="title"]//a[@class="result"]/h2')

    def check_if_redirected(self, search_term):
        if search_term in self.driver.title:
            assert True

    def check_search_results(self, search_term):
        validated = False
        result_items = self.driver.find_elements(*self.SEARCH_RESULT_ITEM_TITLE)
        result_titles_text = []
        for item in result_items:
            if item.is_displayed():
                movie_title = item.text
                result_titles_text.append(movie_title.lower())
        for i in range(len(result_titles_text)):
            if search_term in result_titles_text[i]:
                validated = True
        print(result_titles_text)

        assert validated
