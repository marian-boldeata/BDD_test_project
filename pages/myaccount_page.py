from selenium.webdriver.common.by import By

from browser import Browser

class Myaccount_Page(Browser):

    NAV_BAR_USER_ICON = (By.XPATH,'//a[@aria-label="Profile and Settings"]')


    def check_if_logged(self):
        if self.driver.find_element(*self.NAV_BAR_USER_ICON).is_displayed():
            assert True
        else:
            assert False

