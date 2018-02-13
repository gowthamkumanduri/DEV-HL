from flask import Flask
from flask import request,render_template,redirect
from flask_bootstrap import Bootstrap
from modules import add,db,table
import xlrd,xlwt
from flask import send_from_directory
import mysql.connector as md
app = Flask(__name__)
Bootstrap(app)
file_path="/home/gowtham/Desktop/nginxroot/modules/comments.xlsx"
output_book = xlwt.Workbook()
output_sheet = output_book.add_sheet('data1')
style_string = "font: bold on; "
style = xlwt.easyxf(style_string)
output_sheet.write(0,0,"ID,USERNAME,EMAIL,FIRSTNAME,LASTNAME \n",style=style)
conn = md.connect(user = 'root', password='password', host='localhost', database='testdb')
cursor = conn.cursor()
@app.route("/list",methods=['GET','POST'])
def form():
	if request.method=='GET':
		list1 = []
		sql="SELECT * FROM deletedata"
		cursor.execute(sql)
		for row in cursor:
			list1.append(row)
		print list1
		return render_template('selectform.html',list1=list1)	
	else:
		if request.form['methods']=='DELETE':
			ids=[]
			for k in request.form:
				if k!='methods':
					ids.append(request.form[k])
					#print ids
			query = "DELETE FROM deletedata WHERE ID=%s"
			cursor.execute(query,ids)
			conn.commit()
			return redirect("http://127.0.0.1:5000/list")
		elif request.form['methods']=='EXPORT':
			data = []
			for k in request.form:
				if k!='methods':
					data.append(request.form[k])
					query = "SELECT * FROM deletedata WHERE ID=%s"
					cursor.execute(query,data)
					for row in cursor:
						output_sheet.write(1,0,"{0},{1},{2},{3},{4}\n".format(row[0],row[1],row[2],row[3],row[4]),style=style)
        				output_book.save(file_path)
        				return send_from_directory('file_path',as_attachment=True)
		return "Please select either of DELETE or EXPORT OPTION"




	

@app.route("/add")
def adduser():
	return add()	