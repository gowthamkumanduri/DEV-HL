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
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(1,'gowtham',MD5('123456'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(2,'raghava',MD5('456789'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(3,'sunny',MD5('789123'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(4,'sarath',MD5('111111'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(5,'durga',MD5('222222'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(6,'prasad',MD5('333333'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(7,'raja',MD5('444444'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(8,'vinod',MD5('555555'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(9,'naveen',MD5('666666'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(10,'kumar',MD5('777777'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(11,'murthy',MD5('888888'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(12,'viswanath',MD5('999999'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(13,'bobby',MD5('000000'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(14,'bonthu',MD5('143143'))")
	cursor.execute("INSERT INTO user2(ID,username,password) VALUES(15,'ramesh',MD5('420420'))")
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

	


