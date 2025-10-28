def make_album(artist_name, album_title, num_tracks=None):
    """Return a dictionary of information about a music album."""
    album_info = {
        'artist': artist_name,
        'title': album_title
    }
    if num_tracks:
        album_info['tracks'] = num_tracks
    return album_info

while True:
    print("\nEnter 'q' at any time to quit.")
    
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break
    
    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break
    
    tracks_input = input("Enter the number of tracks (or press Enter to skip): ")
    if tracks_input.lower() == 'q':
        break
    
    if tracks_input.isdigit():
        num_tracks = int(tracks_input)
        album = make_album(artist, title, num_tracks)
    else:
        album = make_album(artist, title)
    
    print("\nAlbum information:")
    for key, value in album.items():
        print(f"{key.title()}: {value}")