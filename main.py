from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page,"html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_titles = []
for movie in movies:
    movies_titles.append(movie.string)

movies = movies_titles[::-1]

with open('movies.txt', 'w', encoding="ISO-8859-1") as file:
    for movie in movies[0:100]:
        file.write(f"{movie}\n")
