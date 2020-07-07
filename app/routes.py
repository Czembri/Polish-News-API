from app import app, lang, pages
from flask import render_template, Blueprint, url_for, redirect, request, Response, send_from_directory, flash, jsonify
import pandas as pd
import csv
from flask_language import current_language
import json
from app.models import DB

# API SECTION
#retreive data from database
gazeta = DB('gazeta')
rmf24 = DB('rmf24')
wp = DB('wp')
tvn24 = DB('tvn24')
interia = DB('interia')

routes = Blueprint('routes', __name__)


@lang.allowed_languages
def get_allowed_languages():
    return ['pl', 'en']

@lang.default_language
def get_default_language():
    return 'pl'

@app.route('/polish-news/api/v1/language')
def get_language():
    return jsonify({
        'language': str(current_language),
    })

@app.route('/polish-news/api/v1/language', methods=['POST'])
def set_language():
    req = request.get_json()
    language = req.get('language', None)

    lang.change_language(language)

    return jsonify({
        'language': str(current_language),
    })

@app.route('/polish-news/api/v1/news', methods=['GET'])
def main():
  sg = gazeta.selectAll()
  sr = rmf24.selectAll()
  sw = wp.selectAll()
  st = tvn24.selectAll()
  si = interia.selectAll()
  return jsonify({'News':'All news in one'}, {'Gazeta':sg, 'rmf24':sr, 'WP':sw, 'TVN24':st, 'Interia':si})


@app.route('/polish-news/api/v1/news/id/<int:id>', methods=['GET'])
def get_by_id(id):
  gazetaID = gazeta.selectByID(id)
  rmfID = rmf24.selectByID(id)
  tvn24ID = tvn24.selectByID(id)
  wpID = wp.selectByID(id)
  interiaID = interia.selectByID(id)

  return jsonify({'List of news': 'By sources, Ids'}, {'Gazeta':gazetaID, 'Rmf24':rmfID, 'TVN24':tvn24ID, 'WP':wpID, 'Interia':interiaID})


@app.route('/polish-news/api/v1/news/source/<string:source>', methods=['GET'])
def get_by_source(source):
  src = DB(source).selectBySRC()
  return jsonify({'news': 'All news selected by source'}, {source:src})


@app.route('/polish-news/api/v1/news/sources', methods=['GET'])
def get_by_sources():
  src = DB('source').selectSRC()
  return jsonify({'sources':src})

# PAGE SECTION

@app.route('/polish-news')
def index():
  return render_template('index.html')

@app.route('/polish-news/get-id', methods=['POST'])
def get_id():
  ID = request.form.get("ID")
  return redirect(url_for('get_by_id', id=ID))

@app.route('/polish-news/get-source', methods=['POST'])
def get_source():
  SOURCE = request.form.get("SOURCE")
  return redirect(url_for('get_by_source', source=SOURCE))