from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# deixar o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# abrir o navegador na página específica
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
dates = [date.text for date in event_dates]
event_text = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = [event.text for event in event_text]
print(dates)
print(events)
event_info = {n: {'time': dates[n], 'name': events[n]} for n in range(5)}
print(event_info)
driver.quit()
