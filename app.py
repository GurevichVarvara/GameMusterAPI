import os
from flask import Flask

app = Flask(__name__.split('.')[0])
app.config['DEBUG'] = bool(os.environ.get('DEBUG', False))


