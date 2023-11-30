from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.amazon.com.br/2280-GREEN-SN350-NVME-WDS100T3G0C/dp/B09DVQQL9G/ref=sr_1_34?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3QSUXSACOD486&keywords=ssd&qid=1697725152&sprefix=ssd%2Caps%2C163&sr=8-34&ufe=app_do%3Aamzn1.fos.4bb5663b-6f7d-4772-84fa-7c7f565ec65b")

reais = driver.find_element(By.CLASS_NAME, value="a-price-whole")
centavos = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"o valor eh R${reais.text},{centavos.text}")
driver.quit()
