# server.py
from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates',  static_url_path='/static', static_folder='static')

@app.route('/url/task')
def task():
    return render_template('task.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
