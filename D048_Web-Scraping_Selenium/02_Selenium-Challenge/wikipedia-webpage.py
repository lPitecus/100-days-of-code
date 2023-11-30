from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

wiki_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
search_bar = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search_bar.click()
search_bar.send_keys(f"{wiki_count.text}")
search_bar.send_keys(Keys.ENTER)
# driver.quit()
