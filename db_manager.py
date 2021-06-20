import sqlite3



class DB_manager:
    def __init__(self):
        self.db = sqlite3.connect('Mail_tracking_bot.sqlite')
        self.sql = self.db.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users (user_id int, position TEXT)")
        self.sql.execute("CREATE TABLE IF NOT EXISTS departures (user_id int, departure_id TEXT)")
        self.db.commit()

    def add_user(self, user_id, position=""):
        self.sql.execute(f"INSERT INTO users VALUES  (?,?)", (user_id, position))

    def user_exist(self, user_id):
        self.sql.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        return self.sql.fetchone()

    def update_user_position(self, user_id, position):
        self.sql.execute(f'UPDATE users SET position = {position} WHERE user_id = "{user_id}"')

    def get_user_position(self, user_id):
        self.sql.execute(f"SELECT position from users WHERE user_id = '{user_id}'")
        return self.sql.fetchone()[0]

    def get_user_departures(self, user_id):
        self.sql.execute(f"SELECT departure_id FROM departures where = '{user_id}'")



db_manager = DB_manager()
db_manager.add_user(709890)

if db_manager.user_exist(709890):
    print("OK")
else:
    print("NON")

db_manager.get_user_position(2)
