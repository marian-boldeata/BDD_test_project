import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys
from browser import Browser
from selenium.webdriver.support.ui import Select




class Base(Browser):

    def click_on(self,locator):
        self.driver.find_element(*locator).click()


    def click_hold(self,locator):
        button = self.driver.find_element(*locator)
        self.action.move_to_element(button).click().perform()

    def hover_over_click_chain(self, locator, locator1='', locator2=''):
        if locator1 == '' and locator2 == '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).click().perform()

        elif locator1 != '' and locator2 == '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).perform()

            element1 = self.driver.find_element(*locator1)
            self.action.move_to_element(element1).click().perform()

        elif locator1 != '' and locator2 != '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).perform()

            element1 = self.driver.find_element(*locator1)
            self.action.move_to_element(element1).perform()

            element2 = self.driver.find_element(*locator2)
            self.action.move_to_element(element2).click().perform()





    def wait_for_element(self,locator):
        wait = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
        wait.click()


    def insert_text(self, locator, text):
        if text == "N/A":
            pass
        else:
            self.driver.find_element(*locator).send_keys(text)


    def deplete_login_attempts(self, username,  user_field,  sign_btn, expected_element):
        depleted = False

        while not depleted:
            self.insert_text(user_field, username)
            self.click_hold(sign_btn)
            if self.driver.find_element(*expected_element).is_displayed():
                depleted = True
                break

        assert depleted


    def filter_option(self, locator, select_text): # not used right now, no element with <select> tag tested so far
        search_filter_bar = self.make_selector(locator)
        search_filter_bar.select_by_visible_text(select_text)

