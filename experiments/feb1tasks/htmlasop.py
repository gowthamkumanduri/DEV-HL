from flask import Flask
from flask import request
import mysql.connector as md

app = Flask(__name__)
@app.route("/",methods=["POST"])

def html():
	conn = md.connect(host = 'localhost' , user = 'root' , password = 'password' , database = 'testdb' )
	cursor = conn.cursor()
	cursor.execute("DROP TABLE IF EXISTS user2")
	cursor.execute("CREATE TABLE user2(ID INT NOT NULL AUTO_INCREMENT,username VARCHAR(25),password CHAR(40),PRIMARY KEY(ID))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(1,'gowtham','123456')")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(2,'raghava',MD5('456789'))")
	
	conn.commit()
	cursor.execute("SELECT * FROM user2")
	data = cursor.fetchall()
	print data
	cursor.close()
	conn.close()
	Id = request.form['Id']
	firstname = request.form['firstname']
	#lastname = request.form['lastname']
	print(Id)
	print(firstname)
	#if request.form['Id'] ==  
	return "<p> Hi Id is "+ Id +" and firstname is "+ firstname +"</p>"

	


