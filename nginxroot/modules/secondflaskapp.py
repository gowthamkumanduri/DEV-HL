from flask import Flask
from flask import request,render_template,redirect
from flask_bootstrap import Bootstrap
from modules import add,db,table
import xlrd,xlwt,requests
from flask import send_from_directory
import mysql.connector as md
from flask_cors import CORS

app = Flask(__name__)
Bootstrap(app)
CORS(app)
app.config['DIR_LOCATION'] = '/home/gowtham/Desktop/nginxroot/modules/'

file_path= app.config['DIR_LOCATION']+'gowthamdata.xls'
output_book = xlwt.Workbook()
output_sheet = output_book.add_sheet('data1',cell_overwrite_ok=True)
style_string = "font: bold on "
style = xlwt.easyxf(style_string)
header = ['ID','USERNAME','EMAIL','FIRSTNAME','LASTNAME']
r=0
c=0
for val in header:
	output_sheet.write(r,c,val)
	c +=1

conn = md.connect(user = 'root', password='password', host='localhost', database='testdb')
cursor = conn.cursor()
global rn
rn = 1
def write_to_file(cursor):
	global rn
	for row in cursor:
		cn=0    		
		for col in row:
		#print col
			output_sheet.write(rn,cn,col)
			cn +=1
		rn +=1
	output_book.save(file_path)

def tableop():
	cursor.execute("SELECT * FROM APPLICATIONEVENTS")
	html = "<table style = 'border: 1px solid black;'><tr><th style = 'border: 1px solid black;border-collapse: collapse;'>APPID</th><th style = 'border: 1px solid black;border-collapse: collapse;'>STATUS</th><th style = 'border: 1px solid black;border-collapse: collapse;'>COMMENT</th></tr>"
	for row in cursor:
		#print type(row)
		html = html + "<tr>"
		for col in row:
			html=html + "<td style = 'border: 1px solid black;border-collapse: collapse;'>" +str(col)+ "</td>"
		html= html + "</tr>"
	html = html + "</table>"
	return "<html><body>"+html+"</body></html>"

def table_op():
	cursor.execute("SELECT * FROM userevents")
	html = "<table style = 'border: 1px solid black;'><tr><th style = 'border: 1px solid black;border-collapse: collapse;'>APPID</th><th style = 'border: 1px solid black;border-collapse: collapse;'>STATUS</th><th style = 'border: 1px solid black;border-collapse: collapse;'>COMMENT</th></tr>"
	for row in cursor:
		#print type(row)
		html = html + "<tr>"
		for col in row:
			html=html + "<td style = 'border: 1px solid black;border-collapse: collapse;'>" +str(col)+ "</td>"
		html= html + "</tr>"
	html = html + "</table>"
	return "<html><body>"+html+"</body></html>"




@app.route("/list",methods=['GET','POST'])
def form():
	if request.method=='GET':
		list1 = []
		sql="SELECT * FROM userdetails"
		cursor.execute(sql)
		for row in cursor:
			list1.append(row)
		#print list1
		return render_template('deleterow.html',list1=list1)	
	else:
		if request.form['methods']=='DELETE':
			
			for k in request.form:
				if k!='methods':
					ids.append(request.form[k])
					#print ids
			query = "DELETE FROM userdetails WHERE id IN ({0})".format(','.join(ids))
			print query
			cursor.execute(query)
			conn.commit()
			return redirect("http://127.0.0.1:5000/list")
		elif request.form['methods']=='UPDATEASCALLED':
			for k in request.form:
				if k!='methods':
					print request.form[k]
					query= "INSERT INTO APPLICATIONEVENTS(APPID,STATUS,COMMENT) VALUES({0},'Called','good')".format(request.form[k])
					print query
					cursor.execute(query)
					conn.commit()
			return tableop()
		elif request.form['methods']=='UPDATEASNOTINTERESTED':
			for k in request.form:
				if k!='methods':
					query= "INSERT INTO APPLICATIONEVENTS(APPID,STATUS,COMMENT) VALUES({0},'NotInterested','good')".format(request.form[k])
					cursor.execute(query)
					conn.commit()
			return tableop()
		elif request.form['methods']=='EXPORT':
			#print request.form
			for k in request.form:
				if k!='methods':
					query = "SELECT * from deletedata where ID={0}".format(request.form[k])
					print query
					cursor.execute(query)
					write_to_file(cursor)
			return send_from_directory(app.config['DIR_LOCATION'],"gowthamdata.xls",as_attachment=True)
    	
			
		return "Please select either of DELETE or EXPORT OPTION"



	

@app.route("/add")
def adduser():
	return add()


@app.route('/delete',methods=['GET'])
def html():
	if request.method=='GET':
		methods = request.args.get('methods')
		userid  = request.args.getlist('text')
		print type(userid)
		print methods
		if request.args.get('methods') =='DELETE':
			query = "DELETE FROM userdetails WHERE id IN ({0})".format(','.join(userid))
			cursor.execute(query)
			print query
			conn.commit()
			list1 = []
			sql="SELECT * FROM userdetails"
			cursor.execute(sql)
			for row in cursor:
				list1.append(row)
			return render_template("deleterow.html",list1=list1)

		elif request.args.get('methods') =='UPDATEASCALLED':
			#format_strings = ','.join(['%s'] * len(userid))
			query= "INSERT INTO userevents(APPID,STATUS,COMMENT) VALUES({0},'Called','good')".format(','.join(userid))
			print query
			cursor.execute(query)
			conn.commit()
			return table_op()

		elif request.args.get('methods') =="UPDATEASNOTINTERESTED":
			query = "INSERT INTO userevents(APPID,STATUS,COMMENT) VALUES({0},'NotInterested','good')".format(','.join(userid))
			cursor.execute(query)
			conn.commit()
			return table_op()
