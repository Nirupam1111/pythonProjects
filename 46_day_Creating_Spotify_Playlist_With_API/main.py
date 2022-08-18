from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

clint_id='e5d94fade1124114998b3684fba364b9'
clint_secret='bd710e75508e46c0a5831765d04a965d'
redirect_uri='http://example.com'
scope= 'playlist-modify-private'

sp=spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=clint_id,
    client_secret=clint_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    show_dialog=True,
    cache_path="token.txt")
)

user_id = sp.current_user()['id']
# print(user_id)


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("h3",class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 '
                                  'lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 '
                                  'u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 '
                                  'u-max-width-230@tablet-only')
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)
all_songs=song_names[4:102]

song_uris = []
year = date.split("-")[0]

for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
