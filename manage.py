# manage.py

from flask import Flask
from main import app as dash_app

server = Flask(__name__)

@server.route('/')
def index():
    return dash_app.index()

if __name__ == '__main__':
    server.run(debug=True)
