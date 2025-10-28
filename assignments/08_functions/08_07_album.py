def make_album(artist_name, album_title, num_tracks=None):
    """Return a dictionary of information about a music album."""
    album_info = {
        'artist': artist_name,
        'title': album_title
    }
    if num_tracks:
        album_info['tracks'] = num_tracks
    return album_info

album1 = make_album('Nba Youngboy', 'Sincerely Kentrell')
album2 = make_album('Rod Wave', 'Pray 4 Love',)
album3 = make_album('Drake', 'Certifiedloverboy')

print(album1)
print(album2)
print(album3)

print(make_album('Lil Tecca', 'We Love You Tecca', 12))
