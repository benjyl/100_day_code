import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# USER ID: 	11165106087
# USERNAME =sys.argv[1]
SPOTIPY_CLIENT_ID = "e0605436aead49bc92bd65c5909cbebd"
SPOTIPY_CLIENT_SECRET = "abfba8cc9be84edcb72d166b1a6a685c"
SPOTIPY_REDIRECT_URI = "http://example.com"

# try:
#     token = util.prompt_for_user_token(USERNAME)
# except:
#     os.remove(f".cache-{USERNAME}")
#     token = util.prompt_for_user_token(USERNAME)
    
# # create spotify object
# spotifyObject = spotipy.Spotify(auth=token)

params={
    "client_id": SPOTIPY_CLIENT_ID,
    "client_secret": SPOTIPY_CLIENT_SECRET,
    "redirect_uri": SPOTIPY_REDIRECT_URI 
}

# scope = "user-library-read"
scope = "playlist-modify-public"
sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, cache_path="token.txt", show_dialog=True))
# results=sp.current_user_saved_tracks()
# for idx, item in enumerate(results["items"]):
#     track=item["track"]
#     print(idx, track["artists"][0]["name"], "-", track["name"] )
user=sp.current_user()
user_id=user["id"]
print(user_id)