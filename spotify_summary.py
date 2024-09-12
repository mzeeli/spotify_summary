"""
Make sure csv files are closed before running

Sometimes when converting from csv to .xlsx the first column "song" gets messed up, just change the column type to text
"""

import os
import json
import pandas as pd

# Find Files
currDir = os.getcwd()
allFiles = os.listdir(currDir)

streamHistoryFiles = [f for f in allFiles if "Streaming_History_Audio_" in f]

# Create DF with all song history
df_allHistory = pd.DataFrame([])

for f in streamHistoryFiles:
    with open(f, 'r', encoding='utf-8') as file:

        data = json.load(file)
        df_data = pd.DataFrame(data)

        df_allHistory = pd.concat([df_allHistory, df_data], ignore_index=True)

# Process DF
# Creates 2 dataframes grouped by song and artist. Both list number of times played and total listening duration
df_bySong = df_allHistory.groupby(['master_metadata_track_name', 'master_metadata_album_artist_name']).agg(
                numTimesPlayed=('master_metadata_track_name', 'size'),
                total_msPlayed=('ms_played', 'sum')
                ).reset_index()
df_bySong['total_minPlayed'] = df_bySong['total_msPlayed'] / 60000
df_bySong['total_hoursPlayed'] = df_bySong['total_msPlayed'] / 3600000

df_bySong.rename(columns={'master_metadata_track_name': 'song'}, inplace=True)
df_bySong.rename(columns={'master_metadata_album_artist_name': 'artist'}, inplace=True)


df_byArtist = df_allHistory.groupby(['master_metadata_album_artist_name']).agg(
                numTimesPlayed=('master_metadata_album_artist_name', 'size'),
                total_msPlayed=('ms_played', 'sum')
                ).reset_index()
df_byArtist['total_minPlayed'] = df_byArtist['total_msPlayed'] / 60000
df_byArtist['total_hoursPlayed'] = df_byArtist['total_msPlayed'] / 3600000

df_byArtist.rename(columns={'master_metadata_album_artist_name': 'artist'}, inplace=True)

# Save to csv
df_bySong.to_csv('sorted_by_song.csv', index=False, encoding='utf_8_sig')  # utf_8_sig to save asian characters
df_byArtist.to_csv('sorted_by_artist.csv', index=False, encoding='utf_8_sig')