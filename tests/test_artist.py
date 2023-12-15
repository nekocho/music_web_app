from lib.artist import *

def test_construct_artists():
    artist = Artist(1, 'Artist name', 'genre')
    assert artist.id == 1
    assert artist.name == 'Artist name'
    assert artist.genre == 'genre'

def test_equal_artists():
    artist1 = Artist(1, 'Artist name', 'genre')
    artist2 = Artist(1, 'Artist name', 'genre')
    assert artist1 == artist2

def test_format_artists():
    artist= Artist(1, 'Artist name', 'genre')
    assert str(artist) == 'Artist(1, Artist name, genre)'