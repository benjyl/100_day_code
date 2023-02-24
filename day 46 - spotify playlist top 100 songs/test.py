import spotipy 
from spotipy.oauth2 import SpotifyOAuth


# USER ID: 	11165106087
# USERNAME =sys.argv[1]
SPOTIPY_CLIENT_ID = "e0605436aead49bc92bd65c5909cbebd"
SPOTIPY_CLIENT_SECRET = "abfba8cc9be84edcb72d166b1a6a685c"
SPOTIPY_REDIRECT_URI = "http://example.com"


scope = "playlist-modify-private"
sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, cache_path="token.txt", show_dialog=True))

user=sp.current_user()
user_id=user["id"]
print(user_id)