import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    # to get the environmental variables
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
    # uri is the playlist id, which has to be extracted from the url
    playlist_uri = playlist_link.split("/")[-1]
    
    data = sp.playlist_tracks(playlist_uri)
    
    # the package boto3 is used to connect between aws environments
    client = boto3.client('s3')
    
    file_name = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket='spotify-etl-project-saheen',
        Key='raw_data/to_be_processed/' + file_name,
        Body=json.dumps(data)                           #json.dumps() will convert the subset of a (data) objects into a json string.
        )