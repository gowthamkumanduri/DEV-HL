from flask import Flask
from flask import request,render_template,redirect,session,url_for
import requests
from flask_bootstrap import Bootstrap
import mysql.connector as md
app = Flask(__name__)
Bootstrap(app)
conn = md.connect(user = 'root',password = 'password',host='localhost', database = 'testdb')
cursor = conn.cursor()

def validate_login(username,password): 
    is_valid = True
    diff_fields = []
    if  (len(username) == 0) :
    	is_valid = False
    	diff_fields.append('username')
    if (len(password) == 0) :
    	is_valid = False
    	diff_fields.append('password')
    return [diff_fields,is_valid]

def validate_application(form_dic):
	is_valid=True
	different_fields = []
	fields = ['userid','firstname','lastname','salary','company']
	for field in fields:
		if len(form_dic[field])==0:
			different_fields.append(field)
	if len(different_fields):
		is_valid=False
	return [different_fields,is_valid]

userdata = []


@app.route("/login",methods=['GET','POST'])
def login():
	if request.method =='GET':
		return render_template('login.html')
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		data = request.form
		result = validate_login(username, password)
		print "result = "
		print result
		print username
		print password
		if result[1]:
			userdata = []
			query = "SELECT * from user where username='{0}' and password=md5('{1}')".format(username,password)
			#query = "SELECT * from user where username='{0}'".format(username)
			print query 
			cursor.execute(query)
			for row in cursor:
				print row[0]
				userdata.append(row[0])
				print userdata
			query1 = "SELECT * from user_profiles where userid={0}".format(userdata[0])
			cursor.execute(query1)
			for row in cursor:
				#print row[1]
				userdata.append(row[1])
				#print userdata
				if len(userdata):
					session['users'] = userdata
			print session['users']
			return redirect("http://127.0.0.1:5000/history")
		else:
			return render_template('login.html',error = result[0])
	
		
@app.route("/history", methods = ['GET','POST'])
def history():
	print "History API Start"
	try:
		print session['users']
		if session['users'] == '' : 
			return redirect("http://127.0.0.1:5000/login")
 	except:
 		return redirect("http://127.0.0.1:5000/login")

	sql = "SELECT *  from applicationloan where userid={0}".format(session['users'][0])
	cursor.execute(sql)
	list1 = []
	for row in cursor:
		list1.append(row)
	print list1
	return render_template('history.html',list1=list1)
	
	
	
@app.route("/applicationloan", methods=['GET','POST'])
def applicationloan():
	print "is session = "
	print session
	print len(session)

	try:
		print session['users']
		if session['users'] == '' : 
			return redirect("http://127.0.0.1:5000/login")
 	except:
 		return redirect("http://127.0.0.1:5000/login")
										 
	if request.method == 'GET':
		return render_template('applicationloan.html')
	elif request.method == 'POST':
		data = request.form
		result = validate_application(data)
		if result[1]:
			userid = request.form['userid']
			firstname = request.form['firstname']
			lastname = request.form['lastname']
			salary = request.form['salary']
			company = request.form['company']
			cursor.execute("INSERT INTO applicationloan(userid,firstname,lastname,salary,company) VALUES (%s,%s,%s,%s,%s)", (userid,firstname,lastname,salary,company))
			conn.commit()
			return redirect("http://127.0.0.1:5000/history")
		else:
			return render_template('applicationloan.html',error=result[0])
					




if __name__ == '__main__':
    app.debug=True
    app.run()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'