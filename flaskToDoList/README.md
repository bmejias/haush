# TODO List with FLASK

Trying to learn Flask by following Louëlla's blog post on building a To-Do List.

https://lovelacecoding.hashnode.dev/build-a-to-do-list-app-using-python-flask-jinja2-and-sql

## Database

Instead of using SQLite I'm using Postgres 16

Create the database with

```sql
CREATE DATABASE todolist;
```

Load the SQL files with

```sh
psql -p 5416 -d todolist -f database/todo.sql
psql -p 5416 -d todolist -f database/insert_data.sql
```

## Running Flask

For some reason, the `flask` command provided by Louëlla didn't work. I use:

```sh
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run
```
