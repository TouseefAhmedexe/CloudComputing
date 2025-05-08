from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
tasks = []  # In-memory list to store tasks

@app.route('/')
def index():
    username = os.getenv('APP_USERNAME', 'Touseef!')
    return render_template('index.html', tasks=tasks, username=username)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
