import psycopg2
def make_conection():
    conn = psycopg2.connect(database='spotify',
                        user="admin",
                        host='localhost',
                        password='admin',
                        port=5432)
    
    return conn.cursor()


# top 5 most played tracks
def get_most_played_track():
    cur = make_conection()
    

    query = """SELECT title, COUNT(*) FROM tracks GROUP BY title ORDER BY COUNT(*) DESC;"""
    cur.execute(query)
    result = cur.fetchmany(5)
    most_played_tracks = {track[0]: track[1] for track in result}

    return most_played_tracks


# Top artists
def top_artist():
    cur = make_conection()

    top_artist_query = """SELECT ar.artist, COUNT(*) FROM artists AS ar
                          JOIN artist_track AS a ON a.artist_id = ar.artist_id
                          JOIN tracks AS t ON a.track_id = t.track_id
                          GROUP BY ar.artist ORDER BY COUNT(*) DESC;"""
    cur.execute(top_artist_query)
    artist_result = cur.fetchmany(5)
    top_artists = {artist[0]: artist[1] for artist in artist_result}

    return top_artists


def top_genres():
    cur = make_conection()

    top_genres_query = """select g.genre, count(*) from genres as g
    group by g.genre order by count(*) desc;"""

    cur.execute(top_genres_query)
    top_genres_query_results = cur.fetchmany(5)

    top_genre = {genre[0]: genre[1] for genre in top_genres_query_results}

    return top_genre


def top_albums():
    cur = make_conection()

    top_album_query = """select a.title, count(*) from album as a 
    join tracks as t on t.album_id = a.album_id
    group by a.title order by count(*) desc; """

    cur.execute(top_album_query)

    top_album_query_result = cur.fetchmany(5)

    top_album = {album[0]: album[1] for album in top_album_query_result}

   

    return top_album


