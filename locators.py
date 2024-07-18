"""
File contains all locators with name format - name_of_page + description_of_locator

"""
from selenium.webdriver.common.by import By


class Locators:

    "HOME PAGE LOCATORS"
    HOME_PAGE_LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Login')
    HOME_PAGE_JOIN_TMDB_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Join TMDB')
    HOME_PAGE_SEARCH_BAR = (By.ID,'inner_search_v4')
    HOME_PAGE_SEARCH_BUTTON = (By.XPATH,'//input[@value="Search"]')

    HOME_PAGE_TRANSLATE_BUTTON = (By.CLASS_NAME,'translate')
    HOME_PAGE_DEFAULT_LANGUAGE_DROP = (By.XPATH,'//label[@for="default_language_popup"]/span[2]')
    HOME_PAGE_DEFAULT_LANGUAGE_FIELD = (By.XPATH,'//div[@id="default_language_popup-list"]//input')
    HOME_PAGE_LANGUAGE_RELOAD = (By.XPATH,'//a[@class="no_click button rounded upcase"]')
    HOME_PAGE_BANNER_TITLE = (By.XPATH,'//div[@class="title"]/h2')

    "LOGIN PAGE LOCATORS"
    LOGIN_PAGE_USERNAME_FIELD = (By.ID, "username")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_PAGE_SUBMIT_LOGIN_BUTTON = (By.ID, "login_button")
    LOGIN_PAGE_OUT_OF_LOGIN_ATTEMPTS = (By.XPATH, '//h2[text()="Out of login attempts"]')

    "SIGNUP PAGE LOCATORS"
    SIGNUP_PAGE_USERNAME_FIELD = (By.ID, 'username')
    SIGNUP_PAGE_PASSWORD_FIELD = (By.ID, 'password')
    SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD = (By.ID, 'password_confirm')
    SIGNUP_PAGE_EMAIL_FIELD = (By.ID, 'email')
    SIGNUP_PAGE_SUBMIT_BUTTON = (By.ID, 'sign_up_button')

    "MY ACCOUNT PAGE LOCATORS"
    MY_ACCOUNT_USER_NAV_DROPDOWN = (By.XPATH, '//a[@aria-label="Profile and Settings"]')
    MY_ACCOUNT_USER_NAV_DROPDOWN_LOGOUT = (By.LINK_TEXT, 'Logout')


    "SEARCH PAGE LOCATORS"
    SEARCH_PAGE_NO_S_RESULTS = (By.XPATH,'//div[@class="search_results movie "]/div/p')
    SEARCH_RESULT_ITEM_TITLE = (By.XPATH, '//div[@class="content_wrapper"]//div[@class="title"]//a[@class="result"]/h2')
    SEARCH_PAGE_FILTER_BAR = (By.XPATH,'//ul[@class="settings panel with_counts scroller"]')
    SEARCH_PAGE_MOVIE_FILTER = (By.ID,'movie')
    SEARCH_PAGE_PEOPLE_FILTER = (By.ID, 'person')
    SEARCH_PAGE_TV_SHOWS_FILTER = (By.ID, 'tv')
    SEARCH_PAGE_COLLECTIONS_FILTER = (By.ID, 'collection')
    SEARCH_PAGE_ITEM_DATA_TYPE = (By.XPATH,'//a[@data-media-type]')
