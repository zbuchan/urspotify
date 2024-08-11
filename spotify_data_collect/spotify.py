import logging
import time
from datetime import datetime
from os import environ

import database
import spotipy
import table_database
from spotipy.oauth2 import SpotifyOAuth

logger = logging.getLogger(__name__)


# creating dictionary for conecting to spotify and postgreql
def get_config():

    config = {}

    config["client_id"] = environ.get("SPOTIPY_CLIENT_ID")
    config["client_secret"] = environ.get("SPOTIPY_CLIENT_SECRET")
    config["redirect_uri"] = environ.get("SPOTIPY_REDIRECT_URI")
    config["db_user"] = environ.get("POSTGRES_USER")
    config["db_password"] = environ.get("POSTGRES_PASSWORD")
    config["db_host"] = environ.get("POSTGRES_HOST")
    config["db_name"] = environ.get("POSTGRES_DB")
    config["db_port"] = 5432

    for key in config:
        if config[key] is None:
            logger.error("Could not find value for: %s", key)
            exit(1)

    return config


# Collects user spotify data
# parameter - config(dictionary with connection values)
def start_collecting_data(config):

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-recently-played"))

    while True:
        db_conn = database.create_connection(config)

        # TODO limit should be configurable
        results = recent_played_tracks(sp, 50)
        process_tracks(results, sp, db_conn)

        # sleep for 60 seconds
        time.sleep(60)
        db_conn.close()


# returns users tracks
# parameters - sp(spotify connection), limit(how many songs to return, limit is 50)
def recent_played_tracks(sp, limit):
    try:
        return sp.current_user_recently_played(limit)
    except Exception as e:
        logger.exception("Could not get list of recently played tacks")


# inserts users spotify data into database
# parameters - results(user song data), sp(spotify connection), db_conn(database connection)
def process_tracks(results, sp, db_conn):

    for i in range(len(results["items"])):
        track_id = results["items"][i]["track"]["id"]

        album_id = results["items"][i]["track"]["album"]["id"]
        track_name = results["items"][i]["track"]["name"]

        time_played = results["items"][i]["played_at"]

        # create timestamp from string
        parsed_date = datetime.fromisoformat(time_played[:-1])

        artist_id = results["items"][i]["track"]["album"]["artists"][0]["id"]
        artists_name = results["items"][i]["track"]["album"]["artists"][0]["name"]

        album_results = sp.album(album_id)
        album_name = results["items"][i]["track"]["album"]["name"]
        total_tracks = album_results["total_tracks"]

        artist_result = sp.artist(artist_id)
        artist_genre = artist_result["genres"]

        database.insert_track_into_data_base(
            track_id, album_id, track_name, parsed_date, db_conn
        )

        database.insert_artist_into_data_base(artist_id, artists_name, db_conn)

        database.insert_album_into_data_base(
            album_id, album_name, total_tracks, db_conn
        )

        database.insert_genre_into_data_base(artist_id, artist_genre, db_conn)

        database.insert_artist_track_into_data_base(track_id, artist_id, db_conn)

        database.insert_artist_genre_into_data_base(artist_id, artist_genre, db_conn)

        database.insert_album_artist_into_data_base(album_id, artist_id, db_conn)


if __name__ == "__main__":
    config = get_config()

    db_conn = database.create_connection(config)
    table_database.create_tables(db_conn)
    db_conn.close()

    start_collecting_data(config)
