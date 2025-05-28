from concert_db import Database

def run_tests():
    db = Database()

    print("Adding artists...")
    artist1_id = db.add_artist("Kendrick Lamar", "Hip-Hop")
    artist2_id = db.add_artist("Rihanna", "Pop")
    artist3_id = db.add_artist("Kendrick Lamar", "Hip-Hop")  

    print(f"Artist IDs: {artist1_id}, {artist2_id}")

    print("\nListing all artists:")
    artists = db.get_artists()
    for artist in artists:
        print(artist)

    print("\nFinding artist by name 'Rihanna':")
    rihanna = db.find_artist_by_name("Rihanna")
    print(rihanna)

    print("\nAdding concerts...")
    concert1_id = db.add_concert(artist1_id, "2025-07-01", "Madison Square Garden")
    concert2_id = db.add_concert(artist2_id, "2025-08-15", "Wembley Stadium")

    print("\nListing all concerts:")
    concerts = db.get_concerts()
    for concert in concerts:
        print(concert)

    print(f"\nDeleting artist ID {artist1_id} (should cascade delete concerts)...")
    db.delete_artist(artist1_id)

    print("\nListing all concerts after deleting artist:")
    concerts = db.get_concerts()
    for concert in concerts:
        print(concert)

    db.close()

if __name__ == "__main__":
    run_tests()
