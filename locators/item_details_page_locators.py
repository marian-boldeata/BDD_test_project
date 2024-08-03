from selenium.webdriver.common.by import By


class Item_details_page_locators():

    ITEM_DETAILS_PAGE_ADD_TO_WATCHLIST = (By.ID, 'watchlist')
    ITEM_DETAILS_PAGE_ITEM_TITLE = (By.XPATH, '//div[@class="title ott_true"]/h2/a')