import os
import spotipy
from spotipy import SpotifyOAuth

scope = "user-library-read playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

CLIENT_USERNAME = os.environ['SPOTIPY_CLIENT_USERNAME']
PLAYLIST_ID = os.environ['RECENT_LIKES_PLAYLIST_ID']
PLAYLIST_LEN = int(os.environ['RECENT_LIKES_PLAYLIST_LEN'])

results = sp.user_playlist_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID)
current_tracks = []
for track in results['items']:
    current_tracks.append(track['track']['uri'])

sp.user_playlist_remove_all_occurrences_of_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID, tracks=current_tracks)

results = sp.current_user_saved_tracks(limit=PLAYLIST_LEN)
recent_likes = []
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    recent_likes.append(track['uri'])

sp.user_playlist_add_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID, tracks=recent_likes)
