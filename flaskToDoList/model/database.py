import psycopg2


class Database(object):
    def __init__(self):
        pass

    def connect_db(self):
        conn = psycopg2.connect(host="localhost",
                                port="5416",
                                dbname="todolist",
                                user="bmejias",
                                application_name="todolist",
                                sslmode="require")
        cursor = conn.cursor()
        return cursor, conn
