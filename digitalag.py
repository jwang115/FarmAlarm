from flask import Flask, session
from flask import g
import json
import itertools
import datetime
from time import strftime
import sqlite3

app = Flask(__name__)

DATABASE = 'schematest.db'#schema.sql'

#DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      cmd = f.read()
      print(cmd)
      #cmd = f.read()
      #print(cmd)
      #print(f.read())
      db.cursor().executescript(cmd)
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""

    init_db()
    print('Initialized the database.')

@app.route('/',methods=['GET', 'POST'])
def getcrops():

  return ""

@app.route('/tools',methods=['GET'])
def tools():
  return "stufff!!!!!\nwhoaaaaaa"
