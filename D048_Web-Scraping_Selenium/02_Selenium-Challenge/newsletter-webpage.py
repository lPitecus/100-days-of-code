from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Arthur")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Silva")
email = driver.find_element(By.NAME, value="email")
email.send_keys("teste@gmail.com")
button = driver.find_element(By.TAG_NAME, value="button")
button.click()
