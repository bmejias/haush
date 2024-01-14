from model.database import Database


class Task():
    def __init__(self):
        database = Database()
        self.cursor, self.conn = database.connect_db()


    def get_tasks(self):
        self.cursor.execute("SELECT * FROM todo.tasks")
        return self.cursor.fetchall()
