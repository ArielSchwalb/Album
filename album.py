def make_album(artist_name, album_title):
    """Return a list of artist names and titles."""
    album = artist_name, album_title
    return album
    
while True:
    print("\nPlease tell me the name of the artist.")
    print("\n(Enter 'q' at any time to quit)")

    artist_name = input("Artist name:") 
    if artist_name == 'q':
        break

    print("\nPlease tell me the name of the album.")
    print("\n(Enter 'q' at any time to quit)")

    album_title = input("Album title:") 
    if album_title == 'q':
        break

    print(f"Artist name: {artist_name}\nAlbum title: {album_title}" )


