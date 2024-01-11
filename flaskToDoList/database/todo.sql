CREATE SCHEMA IF NOT EXISTS todo;

CREATE TABLE IF NOT EXISTS todo.tasks (
      task_id             serial PRIMARY KEY
    , task_name           text NOT NULL
    , task_description    text
    , due_date            timestamptz
    , priority            integer
    , status              text
    , created_at          timestamptz default current_timestamp
);
