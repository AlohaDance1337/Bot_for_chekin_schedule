import sqlite3


class DatabaseHandler:
    def __init__(self):
        self.db_path = 'database.sqlite3'
        self._create_user_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_user_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    number_of_group INTEGER
                )
            ''')
            conn.commit()

    def add_user(self, user_id: int, number_of_group: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (user_id, number_of_group) VALUES (?, ?)', (user_id, number_of_group))
            conn.commit()

    def get_user(self, user_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ? ', (user_id,))
            return cursor.fetchone()
