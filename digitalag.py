from flask import Flask, render_template, session

import json
import itertools
import datetime
from time import strftime

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def getcrops():
  return ""

@app.route('/tools',methods=['GET'])
def tools():
  return "stufff!!!!!\nwhoaaaaaa"
