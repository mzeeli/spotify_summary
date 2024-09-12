# spotifySummary
Sorts through spotify data

At some point, my friends were discussing their most listened to songs, and I remembered that you can actually request Spotify to send you all the data they have on you, including your entire listening history as JSON files. This repo just contains a script to process that data.

To request your full spotify history, go to the bottom of this link and make sure to select 'Extended Streaming History,' otherwise, it will only include data from the last year: https://www.spotify.com/ca-en/account/privacy/

It’ll take them about two weeks to prepare the extended version. Once you receive it, copy the python file into the folder with all the JSON files and run it. The python script will sort the data by artist and song, saving it as a CSV, which you can then edit in Excel. There's also a lot more information in the JSON files, so you can filter by date or do other custom analysis stuff if you want too.

Example of an entry from the JSON:
  {
    "ts": "2023-08-07T21:07:25Z",
    "username": "jirekyberg",
    "platform": "android",
    "ms_played": 108019,
    "conn_country": "CA",
    "ip_addr_decrypted": "72.136.112.157",
    "user_agent_decrypted": "unknown",
    "master_metadata_track_name": "I Want It That Way",
    "master_metadata_album_artist_name": "Backstreet Boys",
    "master_metadata_album_album_name": "Millennium",
    "spotify_track_uri": "spotify:track:47BBI51FKFwOMlIiX6m8ya",
    "episode_name": null,
    "episode_show_name": null,
    "spotify_episode_uri": null,
    "reason_start": "fwdbtn",
    "reason_end": "fwdbtn",
    "shuffle": true,
    "skipped": true,
    "offline": false,
    "offline_timestamp": 1691442338,
    "incognito_mode": false
  },
