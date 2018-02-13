from flask import Flask 
from flask import request
import mysql.connector as md

app = Flask(__name__)
conn = md.connect(host = 'localhost' , user = 'root' , password = 'password' , database = 'testdb' )
cursor = conn.cursor()
cursor.execute("SELECT * FROM user2")
html = "<table style = 'border: 1px solid black;'><tr><th style = 'border: 1px solid black;border-collapse: collapse;'>Id</th><th style = 'border: 1px solid black;border-collapse: collapse;'>username</th><th style = 'border: 1px solid black;border-collapse: collapse;'>password</th></tr>"
for row in cursor:
	#print type(row)
	html = html + "<tr>"
	for col in row:
		html=html + "<td style = 'border: 1px solid black;border-collapse: collapse;'>" +str(col)+ "</td>"
	html= html + "</tr>"
html = html + "</table>"
	
cursor.close()
conn.close()

@app.route("/list", methods = ["GET"])
def table():
	return "<html><body>"+html+"</body></html>"

