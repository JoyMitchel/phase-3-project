from concert_db import Database

def run_tests():
    db = Database()

    print("Adding concerts...")
    db.add_concert("The Beatles", "Wembley Stadium", "2023-07-01", "19:00")
    db.add_concert("Queen", "O2 Arena", "2023-08-15", "20:00")
    db.add_concert("Pink Floyd", "Madison Square Garden", "2023-09-10", "21:00")
    print("Concerts added successfully.")