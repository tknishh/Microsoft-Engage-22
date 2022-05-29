import  pickle as p
import streamlit as st
import pandas as pd
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

cid = 'e5164fbe5751433e874d5fd5b59efc3b'
secret = 'bde09ec2fbe044f689e9b64db6dcf24a'
redirect_uri='http://localhost:8888/callback'
username = 'c3drys7oy7f88tijr6fs0eg0i'


def load():
    global df_list
    global consine_similarities

    if 'df_list' not in globals():
        df_list = pd.read_csv('final_pl.csv')
    if 'consine_similarities' not in globals():
        with open('consine_similarities.pkl','rb') as f:
            consine_similarities = p.load(f)

load()

scope = 'user-top-read playlist-modify-private playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

def create_playlist(consine_similarities):
    playlists = sp.user_playlist_create(username)

# def fetch_playlists(sp, username):
#     """
#     Returns the user's playlists.
#     """
        
#     id = []
#     name = []
#     num_tracks = []
    
#     # Make the API request
#     playlists = sp.user_playlists(username)
#     for playlist in playlists['items']:
#         id.append(playlist['id'])
#         name.append(playlist['name'])
#         num_tracks.append(playlist['tracks']['total'])

#     # Create the final df   
#     df_playlists = pd.DataFrame({"id":id, "name": name, "#tracks": num_tracks})
#     return df_playlists

# playlist_id = fetch_playlists(sp,username)['id'][0]

# def enrich_playlist(sp, username, playlist_id, playlist_tracks):
#     index = 0
#     results = []
    
#     while index < len(playlist_tracks):
#         results += sp.user_playlist_add_tracks(username, playlist_id, tracks = playlist_tracks[index:index + 50])
#         index += 50

# list_track = df.loc[df['prediction']  == 1]['track_id']
# enrich_playlist(sp, username, playlist_id, list_track)



st.title("Song Recommender")
# option = st.selectbox("Enter Any restaurants", res_dist['name'].values)
option = st.selectbox("Enter sny song", df_list['track_id'].values)

if st.button("Recommend"):
      opt = f'{option}'
      recommendation=create_playlist(consine_similarities)(opt)
      for i in recommendation:
       st.write(i)