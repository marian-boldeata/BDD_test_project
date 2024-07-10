from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains


class Browser():

    driver = Driver()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)

    action = ActionChains(driver)



    def close_browser(self):
        self.driver.quit()
