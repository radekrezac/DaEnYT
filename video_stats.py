import requests
from dotenv import load_dotenv
import os   
load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("YOUTUBE_API_KEY")
URL_BASE = os.getenv("YOUTUBE_URL_BASE")

CHANNEL_ID = "MrBeast"
PART = "contentDetails"

def get_channel_uploads_playlist_id(channel_id):

    try:

        url = f"{URL_BASE}channels?part={PART}&forHandle={CHANNEL_ID}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        data = response.json()
        channel_items = data["items"][0]
        channel_playlists = channel_items["contentDetails"]["relatedPlaylists"]
        uploads_playlist_id = channel_playlists["uploads"]

        return uploads_playlist_id
    
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
if __name__ == "__main__":
    print("Getting uploads playlist ID...")
    uploads_playlist_id = get_channel_uploads_playlist_id(CHANNEL_ID)
    print(f"Uploads Playlist ID: {uploads_playlist_id}")      