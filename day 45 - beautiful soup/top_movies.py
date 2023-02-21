from bs4 import BeautifulSoup
import requests

# Create list of top 100 movies from empire

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.encoding="utf-8" # E.t. was improperly formatted,  â\x80\x93 instead of - 
top_movies = response.text
soup = BeautifulSoup(top_movies, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()
# for movie in movies:
#     movie_titles.append(movie.getText())

print(movie_titles)
with open("movies.txt", 'w', encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

# movie_titles = []
# movie_titles=[movie_titles.insert(0, movie.getText()) for movie in movies]
# print(len(movie_titles))
# print(movie_titles)