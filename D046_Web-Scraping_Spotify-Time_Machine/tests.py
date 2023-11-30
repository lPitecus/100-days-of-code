from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.billboard.com/charts/hot-100/2000-04-28/")
response.encoding = "utf-8"
html = response.text

soup = BeautifulSoup(html, "html.parser")
artists = soup.select(selector="li ul li span", class_="c-label")

for artist in artists[::7]:
    print(artist.text.strip())

print(len(artists[::7]))
