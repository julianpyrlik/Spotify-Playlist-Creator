from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Ask user for year
year = input("Which year would you like to travel to? (Format YYYY-MM-DD): ")

# Save URL depending on year
URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)
webpage = response.text

# Webscraping to get the Songlist
soup = BeautifulSoup(webpage, features="html.parser")
songs = soup.select(selector='div ul li ul li h3')
song_list = [element.getText().strip() for element in songs]

print(song_list)
# --------------------------------Spotify------------------------------------------
# CONSTANTS
spotify_id = '85ba2817315a4d03becaae4b04658376'
spotify_secret = '2538a1d6c34d493eada3b760cde1606f'
spotify_redirect_URI = 'http://example.com'

spotify_user_id = '1137868650'
creating_playlist_endpoint = f'https://api.spotify.com/v1/users/{spotify_user_id}/playlists'
scope = "playlist-modify-private"

# ------------------------------------Spotipy-----------------------------------------
# authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id, client_secret=spotify_secret,
                                               redirect_uri=spotify_redirect_URI,
                                               state=None, scope=scope, cache_path=None, username=None, proxies=None,
                                               show_dialog=False, requests_session=True, requests_timeout=None))

# print(sp.current_user())

# Search for the song titles and creating list with song-URIs
uri_list = []

for element in song_list:
    track = sp.search(q=element, limit=1, offset=0, type='track', market=None)
    track_uri = (track['tracks']['items'][0]['uri'])
    uri_list.append(track_uri)

# creating playlist
playlist_name = f'Hits of {year}'
new_playlist = sp.user_playlist_create(user=spotify_user_id, name=playlist_name, public=False,
                                       description="This is a test")
new_playlist_uri = new_playlist['uri']

# adding the songs to the playlist
sp.playlist_add_items(playlist_id=new_playlist_uri, items=uri_list, position=None)
