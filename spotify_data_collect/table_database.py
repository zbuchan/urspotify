import logging

import psycopg2

logger = logging.getLogger(__name__)


# creates database tables
# param = conn(connection)
def create_tables(conn):
    try:
        cur = conn.cursor()

        cur.execute(
            """CREATE TABLE if not exists tracks (
        track_id    varchar(80),
        album_id    varchar(80),
        title       varchar(80),
        played_at   timestamp
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists artists (
        artist_id   varchar(80),
        artist      varchar(80)
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists album (
        album_id        varchar(80),
        title           varchar(80),
        total_tracks    integer     
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists genres (
        genre_id    varchar(80),
        genre       varchar(80)
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists artist_track (
        track_id    varchar(80),
        artist_id   varchar(80)
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists artist_genre (
        artist_id   varchar(80),
        genre_id    varchar(80)
        );"""
        )

        cur.execute(
            """CREATE TABLE if not exists album_artist (
        album_id    varchar(80),
        artist_id   varchar(80)
        );"""
        )

        conn.commit()

    except Exception as e:
        logger.exception("Could not create database tables")
        conn.close()
