import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    # title = request.form['title']
    # release_year = request.form['release_year']
    # artist_id = request.form['artist_id']
    album = Album(
        None,
        request.form['title'], 
        request.form['release_year'], 
        request.form['artist_id'])
    repository.create(album)
    return '', 200

@app.route('/albums', methods=['GET'])
def get_single_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return '\n'.join(
        f"{album}" for album in repository.all()
    )

# CHALLENGE START: ARTISTS

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    list_artist = repository.all()
    artist_name = [artist.name for artist in list_artist]

    join_names = ', '.join(artist_name)
    return join_names, 200

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )
    repository.create(artist)
    return '', 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

