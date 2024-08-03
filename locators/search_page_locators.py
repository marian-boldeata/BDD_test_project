from selenium.webdriver.common.by import By


class Search_page_locators():


    SEARCH_PAGE_NO_S_RESULTS = (By.XPATH, '//div[@class="search_results movie "]/div/p')
    SEARCH_RESULT_ITEM_TITLE = (By.XPATH, '//div[@class="content_wrapper"]//div[@class="title"]//a[@class="result"]/h2')
    SEARCH_PAGE_FILTER_BAR = (By.XPATH, '//ul[@class="settings panel with_counts scroller"]')
    SEARCH_PAGE_MOVIE_FILTER = (By.ID, 'movie')
    SEARCH_PAGE_PEOPLE_FILTER = (By.ID, 'person')
    SEARCH_PAGE_TV_SHOWS_FILTER = (By.ID, 'tv')
    SEARCH_PAGE_COLLECTIONS_FILTER = (By.ID, 'collection')
    SEARCH_PAGE_ITEM_DATA_TYPE = (By.XPATH, '//a[@data-media-type]')