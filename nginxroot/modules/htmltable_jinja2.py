from flask import Flask
from flask import request,render_template
import mysql.connector as md
app = Flask(__name__)

list1 = []

conn = md.connect( user = 'root', password = 'password', host = 'localhost', database = 'testdb')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user2')
for row in cursor:
	if row not in list1:
		list1.append(row)

print type(list1)

@app.route("/table", methods = ["GET"])
def table():
	return render_template('table.html',list1=list1)