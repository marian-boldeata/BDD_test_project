from selenium.webdriver.common.by import By

from browser import Browser


class Home_Page(Browser):


    def go_to_homepage(self):
        self.driver.get('https://www.themoviedb.org/')

    def default_language_select(self, language):
        language_select = self.driver.find_element(By.XPATH,f"//ul[@id='default_language_popup_listbox']/li[contains(text(), '{language}')]")
        language_select.click()

    def switch_back_language(self):#this will switch back to english
        element = self.driver.find_element(By.XPATH,f"//ul[@id='default_language_popup_listbox']/li[@id='w606c9f2-4d62-4ca9-bed1-20cdd97778dd']")
        element.click()

    def language_check(self, language, locator):
        main_page_banner_welcome = {
            '(es-ES)': 'Te damos la bienvenida.',
            '(ro-RO)': 'Bun venit.',
            '(de-DE)': 'Willkommen.'
        }
        if language in main_page_banner_welcome:
            element = self.driver.find_element(*locator)
            element_text = element.text

            assert element_text == main_page_banner_welcome[language], f'Expected : {main_page_banner_welcome[language]}, got {element_text}'
            print(element_text)
        else:
            assert False, f'Language {language} not changed'



