from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Browser():

    driver = Driver()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    action = ActionChains(driver)

    def make_selector(self, locator): # not used right now, no element with <select> tag tested so far
        element = self.driver.find_element(*locator)
        select = Select(element)
        return select

    def close_browser(self):
        self.driver.quit()
