import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url=URL)
movie_web_page=response.text

soup=BeautifulSoup(movie_web_page,'html.parser')
movie_title=soup.find_all(name='h3',class_='title')
# print(movie_title)

list_movies=[]

for movie in movie_title:
    movies=movie.getText()
    list_movies.append(movies)


all_movies=list_movies[::-1]

with open('movies.txt',mode='w') as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
