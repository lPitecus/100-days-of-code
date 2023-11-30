import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.delete_all_cookies()
driver.get("https://tinder.com")
main_page = driver.current_window_handle

time.sleep(5)

cookies = driver.find_element(By.XPATH,
                              value='//*[@id="s1166637769"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
time.sleep(1)
enter_button = driver.find_element(By.XPATH,
                                   value='//*[@id="s1166637769"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
enter_button.click()
time.sleep(5)
google_button = driver.find_element(By.ID, value='s-2046495368')
google_button.click()
time.sleep(7)
# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        # change the control to signin page
        driver.switch_to.window(login_page)
        break

email = driver.find_element(By.TAG_NAME, value='input')
email.send_keys(os.environ.get('EMAIL'))
driver.find_element(By.CLASS_NAME, value='VfPpkd-vQzf8d').click()
time.sleep(5)
