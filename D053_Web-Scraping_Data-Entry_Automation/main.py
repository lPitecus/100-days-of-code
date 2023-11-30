from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.keys import Keys

FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeRCAZkDITbE3-KlStmrKU4uPrC4ilw_ov8vRtzwq1y1d7eLQ/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.92840041113281%2C%22east%22%3A-121.93825758886719%2C%22south%22%3A37.44675175795996%2C%22north%22%3A38.10237762660118%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
response = requests.get(ZILLOW_LINK, headers=headers)
response.raise_for_status()
response.encoding = "utf-8"
site_encoded = response.text
soup = BeautifulSoup(site_encoded, "html.parser")

listings = soup.find_all(name="li div div article div div div div span")
for item in listings:
    print(item)
