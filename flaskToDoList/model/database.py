import psycopg2
import psycopg2.extras


class Database(object):
    def __init__(self):
        pass

    def connect_db(self, cursor_type='default'):
        conn = psycopg2.connect(host="localhost",
                                port="5416",
                                dbname="todolist",
                                user="bmejias",
                                application_name="todolist",
                                sslmode="require")
        if cursor_type == 'default':
            cursor = conn.cursor()
        elif cursor_type == 'DictCursor':
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        else:
            raise Exception("ERROR: Invalid cursor type", cursor_type)
        return cursor, conn
