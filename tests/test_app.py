# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# EXERCISE: ALBUMS

def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/albums', 
    data={'title': 'Voyage', 
          'release_year': '2022', 
          'artist_id': '2'
          })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == '' \
        'Album(1, Doolittle, 1989, 1)\n' \
        'Album(2, Voyage, 2022, 2)'
    
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Album(1, Doolittle, 1989, 1)'


# CHALLENGE START: ARTISTS

def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('UTF-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'


def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql') # forgot to add the seed which caused duplication
    response = web_client.post('/artists', data={
        'name': 'Wild nothing', 
        'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('UTF-8') == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('UTF-8') == '' \
        'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'