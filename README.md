# Recent Likes
Place recently liked Spotify songs into a playlist that's more easily downloaded.

## Create an App
1. Create a new app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Make note of the Client ID and secret.
3. Select `Edit Settings` and add the Redirect URI `http://localhost:9090` and save.

## Create a Playlist
1. Create a playlist with a name like `Recent Likes`.
2. Right-click and select `Share` then `Copy Spotify URI`.

## Environment Setup
1. Install Spotipy with `pip install spotipy --upgrade`
2. Run the commands below, filling in the variables.
3. Run the script with `python update-songs.py`

```sh
export SPOTIPY_CLIENT_ID=''
export SPOTIPY_CLIENT_SECRET=''
export SPOTIPY_REDIRECT_URI='http://localhost:9090'
export SPOTIPY_CLIENT_USERNAME=''
export RECENT_LIKES_PLAYLIST_ID=''
```