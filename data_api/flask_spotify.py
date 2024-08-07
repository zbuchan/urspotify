import db_query
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/track", methods=["GET"])
def spotify_data():

    # making json data
    response_data = {"most_played_tracks": db_query.get_most_played_track()}

    return jsonify(response_data)


@app.route("/artist", methods=["GET"])
def artist():

    # making json data
    response_data = {"top_artists": db_query.top_artist()}

    return jsonify(response_data)


@app.route("/genre", methods=["GET"])
def genre():

    # making json data
    response_data = {"top_genre": db_query.top_genres()}

    return jsonify(response_data)


@app.route("/album", methods=["GET"])
def album():

    # making json data
    response_data = {"top_album": db_query.top_albums()}

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000), debug=True)
