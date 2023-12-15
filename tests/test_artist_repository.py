from lib.artist import *
from lib.artist_repository import *

def test_all_artists(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = ArtistRepository(db_connection)

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_create_artists(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = ArtistRepository(db_connection)

    artist = Artist(None, 'Wild nothing', 'Indie')
    repository.create(artist)

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]
