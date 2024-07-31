from selenium.webdriver.common.by import By

from browser import Browser

class Myaccount_Page(Browser):

    NAV_BAR_USER_ICON = (By.XPATH,'//a[@aria-label="Profile and Settings"]')

    def go_to_myaccount_page(self):
        self.driver.get('https://www.themoviedb.org/u/mbx-bx')


    def check_if_logged(self):
        if self.driver.find_element(*self.NAV_BAR_USER_ICON).is_displayed():
            assert True
        else:
            assert False

    def check_added_item(self, item_name, locator):
        verified = False
        actual_item = self.driver.find_element(*locator).text
        if item_name == actual_item:
            verified = True
        assert verified, f'Adeed item {item_name}  not same as item in watchlist {actual_item}'

    def check_if_removed(self, locator):
        removed = False
        item = self.driver.find_element(*locator)
        self.driver.refresh()
        if not item.is_displayed():
            removed = True

        assert removed, f'{item} has not been deleted'


