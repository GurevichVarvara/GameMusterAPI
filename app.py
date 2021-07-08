import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__.split('.')[0])
app.config['DEBUG'] = bool(os.environ.get('DEBUG', False))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()