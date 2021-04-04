import os
import random
import spotipy
from spotipy import SpotifyOAuth

def handler(event, context):

    CLIENT_USERNAME = os.environ['SPOTIPY_CLIENT_USERNAME']
    PLAYLIST_ID = os.environ['SHUFFLE_PLAYLIST_ID']

    print("Authenticating to Spotify")
    scope = "user-library-read playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    print("Authenticated to Spotify")

    print("Getting playlist tracks.")
    results = sp.user_playlist_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID)
    playlist_tracks = []
    for track in results['items']:
        playlist_tracks.append(track['track']['uri'])

    print("Shuffling tracks.")
    random.shuffle(playlist_tracks)

    print("Clearing playlist.")
    sp.user_playlist_remove_all_occurrences_of_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID, tracks=playlist_tracks)

    print("Adding new order.")
    sp.user_playlist_add_tracks(user=CLIENT_USERNAME, playlist_id=PLAYLIST_ID, tracks=playlist_tracks)

if __name__ == "__main__":
    handler('','')