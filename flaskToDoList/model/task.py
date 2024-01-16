from model.database import Database


class Task():
    def __init__(self):
        database = Database()
        self.cursor, self.conn = database.connect_db('DictCursor')


    def get_tasks(self):
        self.cursor.execute("SELECT task_name FROM todo.tasks")
        return self.cursor.fetchall()


    def get_task(self, task_id):
        query = "SELECT * FROM todo.tasks WHERE task_id = %s"
        self.cursor.execute(query % task_id)
        return self.cursor.fetchone()
