from bs4 import BeautifulSoup
from datetime import datetime
import requests

date_format = "%Y-%m-%d" # format required for website

date_valid = False

while not date_valid:
    date = input("What date would you like to get the top 100 songs from? (Format: YYYY-MM-DD)")
    print(f"Input date: {date}")
    try:
        dateObject = datetime.strptime(date, date_format)
        print(dateObject)
        date_valid=True
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
top_songs = response.text
soup = BeautifulSoup(top_songs, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
song_info = [song.getText().strip() for song in songs]
indices = [i for i,x in enumerate(song_info) if x=="Songwriter(s):"]
song_titles = [song_info[indices[i]-1] for i in range(1, len(indices))]
print(len(indices))
print("Song titles:", song_titles)
print("number of songs: ", len(song_titles))
print(indices)