from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
# lista com a localização dos elementos dos upgrades
upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
# lista com os upgrades antes do tratamento da string
upgrades_list = [upgrade.text for upgrade in upgrades]

timeout = time.time() + 60 * 5
buy_delay = time.time() + 10
can_buy = False
while time.time() < timeout:
    cookie.click()
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

    if time.time() > buy_delay:
        for n in range(len(upgrades) - 1, -1, -1):
            try:
                # Tratamento da string com o upgrade para pegar apenas o valor do upgrade.
                # Está em um try, pois o último valor dos upgrades é vazio, logo o programa deve pulá-lo.
                upgrade_value = int(upgrades_list[n].split("\n")[0].split("-")[1].strip().replace(",", ""))
            except IndexError:
                continue
            if money >= upgrade_value:
                driver.find_elements(By.XPATH, value='//*[@id="store"]/div')[n].click()
                break
        buy_delay = time.time() + 10
cps = driver.find_element(By.ID, value="cps")
print(cps.text)
