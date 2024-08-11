import logging
import time
from datetime import datetime
from os import environ

import spotipy
from spotipy.oauth2 import SpotifyOAuth

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-recently-played"))
    try:
        sp.current_user_recently_played(1)
    except Exception as e:
        logger.exception("Could not get list of recently played tacks")
