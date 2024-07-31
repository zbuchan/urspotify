import logging

import psycopg2

logger = logging.getLogger(__name__)


# creates connection to database
# paramaters - config(dictionary with values to connect to database)
def create_connection(config):
    conn = psycopg2.connect(
        database=config["db_name"],
        user=config["db_user"],
        host=config["db_host"],
        password=config["db_password"],
        port=config["db_port"],
    )

    return conn


# inserting data into the track table ---------------------------------------------------------------------------->


# checks if track is in database
def data_exsists_track(track_id, album_id, name, played_at, conn):

    cur = conn.cursor()

    query = """ SELECT track_id, album_id, title, played_at
                    FROM tracks
                    WHERE track_id=%s and album_id=%s and title=%s and played_at=%s;"""

    params = (track_id, album_id, name, played_at)

    cur.execute(query, params)

    result = cur.fetchone()

    return result


def insert_track_into_data_base(track_id, album_id, name, time, conn):
    cur = conn.cursor()

    print("Table track ------------------------------------->")
    print(track_id)
    print(album_id)
    print(name)
    print(time)
    print("\n")

    # checks if track is already in data base, if not data_exsists == None, inserts into database and if song does not equal same time insert
    if (
        str(data_exsists_track(track_id, album_id, name, time, conn)) == "None"
        or data_exsists_track(track_id, album_id, name, time, conn)[3] != time
    ):

        # inserts
        insert_statement = "INSERT INTO tracks(track_id, album_id, title, played_at ) VALUES(%s,%s,%s,%s)"
        data_to_insert = (track_id, album_id, name, time)
        cur.execute(insert_statement, data_to_insert)

    conn.commit()


# inserting into artist table --------------------------------------------------------->


def insert_artist_into_data_base(artist_id, name, conn):
    cur = conn.cursor()

    print("Table artist ------------------------------------->")
    print(artist_id)
    print(name)
    print("\n")

    if str(data_exsists_artist(artist_id, name, conn)) == "None":

        # inserts
        insert_statement = "INSERT INTO artists(artist_id, artist) VALUES(%s,%s)"
        data_to_insert = (artist_id, name)
        cur.execute(insert_statement, data_to_insert)

    conn.commit()


def data_exsists_artist(artist_id, name, conn):

    cur = conn.cursor()

    query = """ SELECT artist_id, artist
                    FROM artists
                    WHERE artist_id=%s and artist=%s ;"""

    params = (artist_id, name)

    cur.execute(query, params)

    result = cur.fetchone()

    # print(result)

    return result


# inserting into album table ------------------------------------------------------->


def insert_album_into_data_base(album_id, name, total_tracks, conn):
    cur = conn.cursor()

    print("Table album ------------------------------------->")
    print(album_id)
    print(name)
    print(total_tracks)
    print("\n")

    if str(data_exsists_album(album_id, name, total_tracks, conn)) == "None":

        # inserts
        insert_statement = (
            "INSERT INTO album(album_id, title, total_tracks) VALUES(%s,%s,%s)"
        )
        data_to_insert = (album_id, name, total_tracks)
        cur.execute(insert_statement, data_to_insert)

    conn.commit()


def data_exsists_album(album_id, name, total_tracks, conn):
    cur = conn.cursor()

    query = """ SELECT album_id, title, total_tracks
                    FROM album
                    WHERE album_id=%s and title=%s and total_tracks=%s ;"""

    params = (album_id, name, total_tracks)

    cur.execute(query, params)

    result = cur.fetchone()

    # print(result)

    return result


# inserting into genre table ------------------------------------------------------->


def insert_genre_into_data_base(genre_id, name, conn):

    cur = conn.cursor()

    print("Table genre ------------------------------------->")
    print(genre_id)

    for g in name:

        print(g)

        if str(data_exsists_genre(genre_id, g, conn)) == "None":

            # inserts
            insert_statement = "INSERT INTO genres(genre_id, genre) VALUES(%s,%s)"
            data_to_insert = (genre_id, g)
            cur.execute(insert_statement, data_to_insert)

    print("\n")

    conn.commit()


def data_exsists_genre(genre_id, name, conn):
    cur = conn.cursor()

    query = """ SELECT genre_id, genre
                    FROM genres
                    WHERE genre_id=%s and genre=%s ;"""

    params = (genre_id, name)

    cur.execute(query, params)

    result = cur.fetchone()

    # print(result)

    return result


# inserting into artist_track JOIN TABLE  ----------------------------------------------->


def insert_artist_track_into_data_base(track_id, artist_id, conn):
    cur = conn.cursor()

    if str(data_exsists_artist_track(track_id, artist_id, conn)) == "None":

        # inserts
        insert_statement = "INSERT INTO artist_track(track_id, artist_id) VALUES(%s,%s)"
        data_to_insert = (track_id, artist_id)
        cur.execute(insert_statement, data_to_insert)

    conn.commit()


def data_exsists_artist_track(track_id, artist_id, conn):
    cur = conn.cursor()

    query = """ SELECT track_id, artist_id
                    FROM artist_track
                    WHERE track_id=%s and artist_id=%s ;"""

    params = (track_id, artist_id)

    cur.execute(query, params)

    result = cur.fetchone()

    return result


# inserting into artist_genre JOIN TABLE ----------------------------------------------------->


def insert_artist_genre_into_data_base(genre_id, name, conn):
    cur = conn.cursor()

    for g in name:

        if str(data_exsists_artist_genre(genre_id, g, conn)) == "None":

            # inserts
            insert_statement = (
                "INSERT INTO artist_genre(artist_id, genre_id) VALUES(%s,%s)"
            )
            data_to_insert = (genre_id, g)
            cur.execute(insert_statement, data_to_insert)

    conn.commit()


def data_exsists_artist_genre(genre_id, name, conn):
    cur = conn.cursor()

    query = """ SELECT artist_id, genre_id
                    FROM artist_genre
                    WHERE artist_id=%s and genre_id=%s ;"""

    params = (genre_id, name)

    cur.execute(query, params)

    result = cur.fetchone()

    return result


# inserting into album_artist JOIN TABLE --------------------------------------------------------- >


def insert_album_artist_into_data_base(album_id, artist_id, conn):
    cur = conn.cursor()

    if str(data_exsists_album_artist(album_id, artist_id, conn)) == "None":

        # inserts
        insert_statement = "INSERT INTO album_artist(album_id, artist_id) VALUES(%s,%s)"
        data_to_insert = (album_id, artist_id)
        cur.execute(insert_statement, data_to_insert)

    conn.commit()


def data_exsists_album_artist(album_id, artist_id, conn):
    cur = conn.cursor()

    query = """ SELECT album_id, artist_id
                    FROM album_artist
                    WHERE album_id=%s and artist_id=%s ;"""

    params = (album_id, artist_id)

    cur.execute(query, params)

    result = cur.fetchone()

    return result
