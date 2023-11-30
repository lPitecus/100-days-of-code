from bs4 import BeautifulSoup
import requests

news_site = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(news_site, "html.parser")
titles = soup.find_all("span", class_="titleline")
points = soup.find_all("span", class_="score")

pos = 1

# A função zip serve para o for loop passar por duas listas simultaneamente.
# As variáveis temporárias são posicionais, ou seja, a variável title vai pegar da lista titles
# e a variável point da lista points
for title, point in zip(titles, points):
    print(f"{pos}. {title.contents[0].text} with {point.contents[0].text}\n")
    pos += 1
