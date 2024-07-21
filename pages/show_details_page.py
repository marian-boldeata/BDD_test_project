from selenium.webdriver.common.by import By

from browser import Browser


class Show_Details_Page(Browser):

    def store_added_item(self, locator):
        added = self.driver.find_element(*locator)
        item_title = added.text
        return item_title



