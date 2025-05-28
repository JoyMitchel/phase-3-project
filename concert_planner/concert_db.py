import sqlite3

class Database:
    def __init__(self, db_name='concerts.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS concerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                artist TEXT NOT NULL,
                venue TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_concert(self, artist, venue, date, time):
        self.cursor.execute('''
            INSERT INTO concerts (artist, venue, date, time)
            VALUES (?, ?, ?, ?)
        ''', (artist, venue, date, time))
        self.connection.commit()

    def get_concerts(self):
        self.cursor.execute('SELECT * FROM concerts')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()