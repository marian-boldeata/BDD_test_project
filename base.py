import time
from browser import Browser


class Base(Browser):

    def click_on(self,locator):
        self.driver.find_element(*locator).click()

    def click_hold(self,locator):
        button = self.driver.find_element(*locator)
        self.action.move_to_element(button).perform()
        time.sleep(0.5)
        self.action.click(button).perform()

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

