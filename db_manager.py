import sqlite3


class DB_manager:
    def __init__(self):
        self.db = sqlite3.connect('Mail_tracking_bot.sqlite', check_same_thread=False)
        self.sql = self.db.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users (user_id TEXT, position TEXT)")
        self.sql.execute(
            "CREATE TABLE IF NOT EXISTS departures (user_id TEXT, departure_id TEXT, departure_short_report TEXT, departure_full_report TEXT)")
        self.db.commit()

    def add_user(self, user_id, position="None"):
        self.sql = self.db.cursor()
        self.sql.execute(f"INSERT INTO users VALUES  (?,?)", (user_id, position))
        self.db.commit()

    def user_exist(self, user_id):
        self.sql.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        return self.sql.fetchone()

    def update_user_position(self, user_id, position):
        self.sql.execute(f'UPDATE users SET position = "{position}" WHERE user_id = "{user_id}"')

    def get_user_position(self, user_id):
        self.sql.execute(f"SELECT position from users WHERE user_id = '{user_id}'")
        return self.sql.fetchone()

    def get_user_departures(self, user_id):
        self.sql.execute(f"SELECT departure_id FROM departures WHERE user_id = '{user_id}'")
        return self.sql.fetchall()

    def add_user_departures(self, user_id, departure_id, departure_short_report="None",):
        self.sql.execute(f"INSERT INTO departures VALUES  ('{user_id}', '{departure_id}', '{departure_short_report}')")
        self.db.commit()

    def debug_info(self):
        self.sql.execute(f"SELECT * from users")
        print(self.sql.fetchall())
