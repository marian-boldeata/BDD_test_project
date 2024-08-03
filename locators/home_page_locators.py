from selenium.webdriver.common.by import By


class Home_page_locators():

    HOME_PAGE_LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Login')
    HOME_PAGE_JOIN_TMDB_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Join TMDB')
    HOME_PAGE_SEARCH_BAR = (By.ID, 'inner_search_v4')
    HOME_PAGE_SEARCH_BUTTON = (By.XPATH, '//input[@value="Search"]')

    HOME_PAGE_TRANSLATE_BUTTON = (By.CLASS_NAME, 'translate')
    HOME_PAGE_DEFAULT_LANGUAGE_DROP = (By.XPATH, '//label[@for="default_language_popup"]/span[2]')
    HOME_PAGE_DEFAULT_LANGUAGE_FIELD = (By.XPATH, '//div[@id="default_language_popup-list"]//input')
    HOME_PAGE_LANGUAGE_RELOAD = (By.XPATH, '//a[@class="no_click button rounded upcase"]')
    HOME_PAGE_BANNER_TITLE = (By.XPATH, '//div[@class="title"]/h2')