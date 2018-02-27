from flask import Flask
from flask import request,render_template,redirect,session,url_for
import requests
from flask_bootstrap import Bootstrap
import mysql.connector as md
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Bootstrap(app)
conn = md.connect(user = 'root',password = 'password',host='localhost', database = 'testdb')
cursor = conn.cursor()

@app.route("/select",methods=['GET','POST'])
def form():
	if request.method=='GET':
		list1 = []
		sql="SELECT * FROM userdetails"
		cursor.execute(sql)
		for row in cursor:
			list1.append(row)
		#print list1
		return render_template('selectform.html',list1=list1)	
	else:
		if request.form['methods']=='DELETE':
			ids=[]
			for k in request.form:
				if k!='methods':
					ids.append(request.form[k])
					#print ids
			query = "DELETE FROM userdetails WHERE id IN ({0})".format(','.join(ids))
			print query
			cursor.execute(query)
			conn.commit()
			return redirect("http://127.0.0.1:5000/select")