from flask import Flask, render_template
from model.task import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<p>Hello Patagonia!</p>'


@app.route('/overview')
def overview():
    task_model = Task()
    all_tasks = task_model.get_tasks()
    return render_template("overview.html", all_tasks=all_tasks)


@app.route('/task/<task_id>')
def show_task(task_id):
    task_model = Task()
    single_task = task_model.get_task(task_id)
    return render_template("task.html", single_task=single_task)


if __name__ == '__main__':
    app.run(debug=True)
