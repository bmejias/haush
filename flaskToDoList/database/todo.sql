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

-- Inserting the first task
INSERT INTO tasks (task_name, task_description, due_date, priority, status)
VALUES ('Complete Project Report'
    , 'Finish writing and editing the project report'
    , '2023-01-31 18:00:00'
    , 2
    , 'To Do'
);

-- Inserting the second task
INSERT INTO tasks (task_name, task_description, due_date, priority, status)
VALUES ('Prepare Presentation'
    , 'Create slides for the project presentation'
    , '2023-02-15 14:30:00'
    , 1
    , 'In Progress'
);
