import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3702564768&f_AL=true&geoId=106057199&keywords=python%20developer&location=Brasil&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R")

time.sleep(3)
sign_in_button = driver.find_element(By.CLASS_NAME,
                                     value='mt-3')
print(sign_in_button.text)
sign_in_button.click()
time.sleep(2)
email = driver.find_element(By.ID, value='username')
email.send_keys(os.environ.get('EMAIL'))
password = driver.find_element(By.ID, value='password')
password.send_keys(os.environ.get('PASSWORD'))
sign_in_button2 = driver.find_element(By.CLASS_NAME, value='from__button--floating')
sign_in_button2.click()
time.sleep(4)
chats = driver.find_element(By.XPATH, value='/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
chats.click()
time.sleep(2)
job_links = driver.find_elements(By.CLASS_NAME, value='job-card-list__title')
for job in job_links:
    job.click()
    time.sleep(5)
    save_button = driver.find_element(By.CSS_SELECTOR, value='.mt5 .display-flex .jobs-save-button span')
    save_button.click()
    time.sleep(5)
    dismiss_button = driver.find_element(By.XPATH, value='/html/body/div[1]/section/div/div/button')
    dismiss_button.click()
    time.sleep(4)
jobs = [job.text for job in job_links]
print(jobs)
