from flask import Flask
from flask import request,render_template,redirect
from flask_bootstrap import Bootstrap
import mysql.connector as md
app = Flask(__name__)
Bootstrap(app)
conn 	= md.connect(user = 'root',password = 'password',host = 'localhost', database = 'testdb')
cursor	= conn.cursor()
@app.route("/loanapplication/add")
def add():
	return render_template('addform.html')

@app.route("/loanapplication", methods = ["POST"])
def db():
	if request.method=='POST':
		User = request.form['User']
		Loancat = request.form['Loancat']
		Firstname= request.form['Firstname']
		Lastname= request.form['Lastname']
		Middlename=request.form['Middlename']
		Dob = request.form['Dob']
		Gender= request.form['Gender']
		State= request.form['State']
		City= request.form['City']
		Pincode=request.form['Pincode']
		Address=request.form['Address']
		Pannumber=request.form['Pannumber']
		Nonlistedcompanyname=request.form['Nonlistedcompanyname']
		cursor.execute("INSERT INTO user3(User,Loancat,Firstname,Lastname,Middlename,Dob,Gender,State,City,Pincode,Address,Pannumber,Nonlistedcompanyname) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (User,Loancat,Firstname,Lastname,Middlename,Dob,Gender,State,City,Pincode,Address,Pannumber,Nonlistedcompanyname))
		conn.commit()
	return redirect("http://127.0.0.1:5000/loanapplication")

@app.route("/loanapplication", methods = ["GET"])

def table():
	list1=[]
	cursor.execute("SELECT * FROM user3")
	#data = cursor.fetchall()
	#print data
	for row in cursor:
		if row not in list1:
			list1.append(row)
	print (list1)
	return render_template('bsform.html',list1=list1)

@app.route("/delete",methods = ["POST"])
def delete():
	del_row=request.form['user']
	print (del_row)
	cursor.execute("DELETE FROM user3 where user = %s ", [del_row])
	conn.commit()
	return redirect("http://127.0.0.1:5000/loanapplication")
	#return "hello"