from flask import Flask
from flask_language import Language
from flask_flatpages import FlatPages


app = Flask(__name__)
lang = Language(app)
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app.config['SECRET_KEY'] = '253fc3280dd1d06014911ee6dcde4382'
app.config.from_object(__name__)
pages = FlatPages(app)

from app import routes