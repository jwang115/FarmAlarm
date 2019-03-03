from flask import Flask, session, jsonify, request, render_template, g
from sqlite3 import dbapi2 as sqlite3
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
  
conn = sqlite3.connect('asdf.db')
print("Opened database successfully");
conn.execute('CREATE TABLE IF NOT EXISTS OtherCrops (IDCroprawr TEXT, ListofCustomersrawr TEXT)')
print("Table created successfully");
conn.close()













@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()          
        
def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schematest.db', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()    

@app.route('/',methods=['GET', 'POST'])
###### SCREEN 3C ######
def getprofile():
  # Precondition: 
  # Postcondition: gets information about their profile for consumers
  conn = sqlite3.connect('schematest.db')
  print("Opened database successfully");
  conn.execute("DELETE from COMPANY where ID = 2;")
  conn.commit()
  print("Total number of rows deleted :", conn.total_changes);  
  '''
  if request.method == 'GET':
      try:
         IDCrop = request.form['IDCrop']
         List = request.form['List of Customers']    
         with sql.connect("schematest.db") as con:
            cur = con.cursor()            
            cur.execute("INSERT INTO students (IDCrop,List) VALUES (?,?)",(IDCrop,List,) )            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"    
      finally:
         con.close()
         con = sql.connect("schematest.db")
         con.row_factory = sql.Row
         cur = con.cursor()
         cur.execute("select * from students")
         rows = cur.fetchall();
         return render_template("list.html",rows = rows)         
    '''
@app.route('/find_user')
def find_user_by_name():
	name = request.args.get('name', '')
	student = find_student(name)
	return jsonify(name=student['name'], age=student['age'], sex=student['sex'])


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      cmd = f.read()
      print(cmd)
      cmd = f.read()
      print(cmd)
      print(f.read())
      db.cursor().executescript(cmd)
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    
    init_db()
    print('Initialized the database.')

def getcrops():
    return ""

# Jeremy starts
###### SCREEN 1C ###### ###### SCREEN 2P ######
def search(items):
  # Precondition:
  # Postcondition: searches for items and returns a list of vendors that sell it based on distance
  pass



###### SCREEN 1P ######
def heatmap(): # item
  # Precondition: 
  # Postcondition: returns a list of locations that have searched for a given item
  pass









@app.route('/tools',methods=['GET'])
def tools():
  return "stufff!!!!!\nwhoaaaaaa"
'''
# EXTRA FUNCTIONS
###### SCREEN 3C ######
def getimages():
  # Precondition: 
  # Postcondition:  
  pass
  
def post():
  # Precondition: 
  # Postcondition: allows to user to post information they want to consumers
  pass

def subscribe():
  # Precondition: 
  # Postcondition: allows the consumer to subscribe to a farmer
  pass

###### SCREEN 4C ######
def getnotify(): # subscribe_list
  # Precondition: 
  # Postcondition:
    # Notify the user when an item they are subsribed to is avaible and notifys them on
    # a home page
  pass
'''