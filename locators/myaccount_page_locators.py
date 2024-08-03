from selenium.webdriver.common.by import By


class Myaccount_page_locators():

    MY_ACCOUNT_USER_NAV_DROPDOWN = (By.XPATH, '//a[@aria-label="Profile and Settings"]')
    MY_ACCOUNT_USER_NAV_DROPDOWN_LOGOUT = (By.LINK_TEXT, 'Logout')
    MY_ACCOUNT_USER_NAV_DROPDOWN_WATCHLIST = (By.XPATH,
                                              '//div[@class="k-widget k-tooltip k-tooltip-closable k-popup k-group k-reset k-state-border-up tmdb_theme_white no_pad"]/div[1]/div/div//p[4]/a')

    MY_ACCOUNT_USER_TOGGLE_MOVIES = (By.XPATH, '//h3//a[@data-media-type="movie"]')
    MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE = (By.XPATH, '//div[@class="title"]/div/a')
    MY_ACCOUNT_USER_WATCHLIST_MOVIE_CARD = (
    By.XPATH, '//div[@id="results_page_1"]/div[@data-object-id="6371aa49e9c0dc007ffcc26a"]')

    MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE_REMOVE = (By.XPATH, '//div[@class="action_bar"]/ul/li[4]/a')
    MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE_ADD_TO_FAV = (By.XPATH, '//div[@class="action_bar"]/ul/li[2]/a')

    MY_ACCOUNT_USER_SHORTCUTBAR_WATCHLIST_DROPDOWN = (By.XPATH, '//span[contains(text(), "Watchlist")]')
    MY_ACCOUNT_USER_SHORTCUTBAR_WATCHLIST_MOVIES = (By.XPATH, '//ul[@id="new_shortcut_bar"]/li[5]//li[1]')

    MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_DROPDOWN = (By.XPATH, '//span[contains(text(), "Overview")]')
    MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_DROPDOWN = (By.XPATH, '//span[contains(text(), "Favourites")]')
    MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_MOVIES_DROPDOWN = (By.XPATH, '//a[@href="/u/mbx-bx/favorites"]')

    MY_ACCOUNT_USER_OVERVIEW_FAVOURITES_FIRST_TITLE = (
    By.XPATH, '//div[@id="card_movie_6371aa49e9c0dc007ffcc26a"]//div[@class="title"]/div/a')