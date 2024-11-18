import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tidalapi
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Load environment variables from .env file
load_dotenv()

# Securely load credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
TIDAL_USERNAME = os.getenv('TIDAL_USERNAME')
TIDAL_PASSWORD = os.getenv('TIDAL_PASSWORD')

# Validate credentials
if not all([SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, TIDAL_USERNAME, TIDAL_PASSWORD]):
    raise ValueError("Missing one or more required environment variables. Check your .env file.")

# TIDAL Login
def tidal_login():
    session = tidalapi.Session()
    session.login(TIDAL_USERNAME, TIDAL_PASSWORD)
    return session

# Spotify Login
def spotify_login():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-read-private"
    ))
    return sp

# Fetch All Spotify Playlists
def get_spotify_playlists(sp):
    playlists = sp.current_user_playlists()
    playlist_data = []
    while playlists:
        for playlist in playlists['items']:
            playlist_data.append({
                'id': playlist['id'],
                'name': playlist['name'],
                'owner': playlist['owner']['display_name']
            })
        playlists = sp.next(playlists)
    return playlist_data

# Fetch Spotify Tracks for a Playlist
def get_spotify_tracks(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name']
        })
    return tracks

# Fetch Existing Tracks in TIDAL
def get_tidal_tracks(session):
    existing_tracks = set()
    favorites = session.user.favorites.tracks()
    for track in favorites:
        track_key = f"{track.name.lower()}:{track.artist.name.lower()}"
        existing_tracks.add(track_key)
    return existing_tracks

# Add a Single Track to TIDAL
def add_track_to_tidal(session, track, existing_tracks):
    track_key = f"{track['name'].lower()}:{track['artist'].lower()}"
    if track_key in existing_tracks:
        return f"Skipping (already in TIDAL): {track['name']} by {track['artist']}"
    
    try:
        search_results = session.search('track', f"{track['name']} {track['artist']}")
        if search_results['tracks']['items']:
            tidal_track = search_results['tracks']['items'][0]
            session.user.favorites.add_track(tidal_track.id)
            return f"Added to TIDAL: {track['name']} by {track['artist']}"
        else:
            return f"Track not found on TIDAL: {track['name']} by {track['artist']}"
    except Exception as e:
        return f"Error adding track: {track['name']} - {e}"

# Sync Tracks to TIDAL Using Threading
def sync_to_tidal(session, tracks, existing_tracks):
    results = []
    added_count = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_track = {
            executor.submit(add_track_to_tidal, session, track, existing_tracks): track for track in tracks
        }
        for future in as_completed(future_to_track):
            result = future.result()
            print(result)
            if "Added to TIDAL" in result:
                added_count += 1
            results.append(result)

    print(f"Sync complete. {added_count} tracks added to TIDAL.")
    return results

# Main Sync Function
def main():
    sp = spotify_login()
    tidal_session = tidal_login()

    print("Fetching all saved Spotify playlists...")
    playlists = get_spotify_playlists(sp)

    print(f"Found {len(playlists)} playlists.")
    for playlist in playlists:
        print(f"Processing playlist: {playlist['name']} (Owner: {playlist['owner']})")
        spotify_tracks = get_spotify_tracks(sp, playlist['id'])
        
        print(f"Fetching existing TIDAL tracks...")
        tidal_existing_tracks = get_tidal_tracks(tidal_session)

        print(f"Syncing playlist '{playlist['name']}' to TIDAL...")
        sync_to_tidal(tidal_session, spotify_tracks, tidal_existing_tracks)

if __name__ == "__main__":
    main()
