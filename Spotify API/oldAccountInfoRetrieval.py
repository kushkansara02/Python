# This script gets information on the playlists and shows of a user and
# deposits the information into text files in the form of dictionaries.
# This can then be used to copy all playlists/shows onto another account.

from spotipy_client import SpotipyClient
import json

# information unique to each user - needed for authentication
username = "your username"
client_id = "your client id"
client_secret = "your client secret"
redirect_uri = "https://google.ca/" #example redirect uri

### GET DATA ON WHAT PODCASTS/PLAYLISTS NEED TO BE COPIED FROM OLD ACCOUNT ###

user = SpotipyClient(username, client_id, client_secret, redirect_uri) # creating new user object
playlists = user.getUserPlaylists()
shows = user.getUserShows()
tracks = {}

playlists_to_be_copied = []
playlists_to_be_followed = []

# iterate through each playlist of the user
for playlist_name in playlists.keys():
    playlist_id = playlists[playlist_name]
    
    if user.getPlaylistOwnerID(playlist_id) == username:
        #if playlist is owned, then this playlist has to be copied
        
        playlists_to_be_copied.append([playlist_name, playlist_id])
    
    else:
        #if playlist is not owned, then this playlist has to be followed
        playlists_to_be_followed.append([playlist_name, playlist_id])

for playlist_name in playlists.keys():
    playlist_id = playlists[playlist_name]
    
    tracks[playlist_name] = user.get_playlist_tracks(playlist_id)

# export data acquired to a text file

with open("playlists_add.txt", "w+") as playlists_file:
    playlists_file.writelines(json.dumps(playlists_to_be_copied))
    
with open("playlists_follow.txt", "w+") as playlists_file:
    playlists_file.writelines(json.dumps(playlists_to_be_followed))

with open("shows.txt", "w+") as shows_file:
    shows_file.writelines(json.dumps(shows))

with open("tracks.txt", "w+") as tracks_file:
    tracks_file.writelines(json.dumps(tracks))
    
print("Process Completed")

### END REGION ###
