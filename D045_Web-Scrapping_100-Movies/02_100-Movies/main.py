import requests
from bs4 import BeautifulSoup

site = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
site.encoding = "utf-8"
site_encoded = site.text
soup = BeautifulSoup(site_encoded, "html.parser")

movie_titles = soup.find_all("h3", class_="title")
movie_list = [title.text for title in movie_titles]

for movie in reversed(movie_list):
    with open("movies.txt", mode="a", encoding="utf-8") as movie_file:
        movie_file.write(f"{movie}\n")
