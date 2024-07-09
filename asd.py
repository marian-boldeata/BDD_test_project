import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumbase import Driver


SIGNUP_USERNAME_FIELD = (By.ID,'username')
SIGNUP_BUTTON = (By.ID,'sign_up_button')

driver = Driver()



driver.get("https://www.themoviedb.org/signup")

driver.find_element(*SIGNUP_USERNAME_FIELD).send_keys("mbx-bx")

driver.find_element(*SIGNUP_USERNAME_FIELD).send_keys(Keys.ENTER)


time.sleep(1)
elements = driver.find_elements(By.XPATH,'//div[@class="carton"]/div/ul')

for item in elements:
    error_text = item.text
    print(error_text)


time.sleep(1)

driver.quit()
