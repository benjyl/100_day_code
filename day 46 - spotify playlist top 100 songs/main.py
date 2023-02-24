from bs4 import BeautifulSoup
from datetime import datetime
import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "e0605436aead49bc92bd65c5909cbebd"
SPOTIPY_CLIENT_SECRET = "abfba8cc9be84edcb72d166b1a6a685c"
SPOTIPY_REDIRECT_URI = "http://example.com"

date_format = "%Y-%m-%d" # format required for website

date_valid = False # check if date valid

# get valid date that user wants top 100 songs from
while not date_valid:
    date = input("What date would you like to get the top 100 songs from? (Format: YYYY-MM-DD)")
    # print(f"Input date: {date}")
    try:
        dateObject = datetime.strptime(date, date_format)
        # print(dateObject)
        date_valid=True
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

# web scrape billboard for the top 100 songs on given date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
top_songs = response.text

# extract HTML data
soup = BeautifulSoup(top_songs, "html.parser")

# songs all under h3 tag with id=title-of-a-story and class: c-title
# other  items beyond story stored under these combined tags too: producers, songwriters etc
web_info = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")

# strip any useless tags e.g. \n 
song_info = [song.getText().strip() for song in web_info]

# Find all songwriter(s) indices, are 101 indices and from index 1-100, the song name is the preceeding index
indices = [i for i,x in enumerate(song_info) if x=="Songwriter(s):"]
song_titles = [song_info[indices[i]-1] for i in range(1, len(indices))]

#Access spotipy
scope = "playlist-modify-private" # for creation of private playlist

#Authentication
sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, cache_path="token.txt", show_dialog=True))

user=sp.current_user()
user_id=user["id"]

song_uris = [] # list of Spotify URIs for available songs
for song in song_titles:

    # use q kwarg with f string format f"track{song} year{year}", type="track" to get valid results
    # don't use q = params where params = {track: song, year: year}    
    results = sp.search(q=f"track: {song} year:{dateObject.year}", type="track")

    try:
        uri = results["tracks"]["items"][0]["uri"] # get sportify uri for each track
        song_uris.append(uri)
    except:
        print(f"{song}: not available on spotify")

# Create new playlist
playlist = sp.user_playlist_create(user_id, f"{dateObject.date()} Billboard top 100 playlist", public=False, collaborative=False,
                        description="Playlist of billboard top 100")

# must pass tracks as a list
# Even single song must have be of format [song_uri]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris, position=None)

