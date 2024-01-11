from model.database import Database


class Task():
    def __init__(self):
        database = Database()
        self.cursor, self.conn = database.connect_db()
