from flask import Flask
from flask import request,render_template
import mysql.connector as md
app = Flask(__name__)
conn 	= md.connect(user = 'root',password = 'password',host = 'localhost', database = 'testdb')
cursor	= conn.cursor()
@app.route("/loanapplication/add")
def add():
	return render_template('form.html')

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
	return 'done'

@app.route("/loanapplication/table", methods = ["GET"])

def table():
	html = "<table style = 'border: 1px solid black;'><tr><th style = 'border: 1px solid black;border-collapse: collapse;'>User</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Loancat</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Firstname</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Lastname</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Middlename</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Dob</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Gender</th><th style = 'border: 1px solid black;border-collapse: collapse;'>State</th><th style = 'border: 1px solid black;border-collapse: collapse;'>City</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Pincode</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Address</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Pannumber</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Nonlistedcompanyname</th></tr>"
	cursor.execute("SELECT * FROM user3")
	#data = cursor.fetchall()
	#print data
	for row in cursor:
		print type(row)
		html = html + "<tr>"
		for col in row:
			html=html + "<td style = 'border: 1px solid black;border-collapse: collapse;'>" +str(col)+ "</td>"
		html= html + "</tr>"
	html = html + "</table>"
	return "<html><body>"+html+"</body></html>"




"""
cursor.execute('SELECT * FROM user2')
#data = cursor.fetchall()
#print data
html = "<table style = 'border: 1px solid black;'><tr><th style = 'border: 1px solid black;border-collapse: collapse;'>User</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Loancat</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Firstname</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Lastname</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Middlename</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Dob</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Gender</th><th style = 'border: 1px solid black;border-collapse: collapse;'>State</th><th style = 'border: 1px solid black;border-collapse: collapse;'>City</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Pincode</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Address</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Pannumber</th><th style = 'border: 1px solid black;border-collapse: collapse;'>Nonlistedcompanyname</th></tr>"
for row in cursor:
	print type(row)
	html = html + "<tr>"
	for col in row:
		html=html + "<td style = 'border: 1px solid black;border-collapse: collapse;'>" +str(col)+ "</td>"
	html= html + "</tr>"
html = html + "</table>"
	#return "<html><body>"+html+"</body></html>"

def table():
	return "<html><body>"+html+"</body></html>"	 """