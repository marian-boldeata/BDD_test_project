from seleniumbase import Driver


class Browser():

    driver = Driver()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)

    def close_browser(self):
        self.driver.quit()