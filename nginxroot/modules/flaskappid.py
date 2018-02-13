from flask import Flask
from flask import request,render_template,redirect
from flask_bootstrap import Bootstrap
import mysql.connector as md
app = Flask(__name__)
Bootstrap(app)
conn = md.connect(user = 'root',password = 'password',host='localhost', database = 'testdb')
cursor = conn.cursor()


def validate_data(form_dic): 
    is_valid = True
    diff_fields = []
    fields = ['Firstname','Salary','Companyname','Loanamount','Pincode','Phone']
    for field in fields:
        if len(form_dic[field])==0:   
            diff_fields.append(field)
    if len(diff_fields):
        is_valid = False 
    return [diff_fields,is_valid]



@app.route("/add")
def add():
	return render_template('useraddform.html')


@app.route("/application",methods = ["GET","POST"])
def db():
    if request.method == 'GET':
        cursor.execute("SELECT appid FROM formdata")
        appid=cursor.lastrowid
        print appid
        return str(appid) 
    elif request.method == 'POST':
        data = request.form
        result = validate_data(data) 
        if result[1]:

            Firstname = request.form['Firstname']
            Lastname = request.form['Lastname']
            Salary= request.form['Salary']
            Companyname= request.form['Companyname']
            Tenure=request.form['Tenure']
            Loanamount = request.form['Loanamount']
            Pincode= request.form['Pincode']
            Phone=request.form['Phone']
            Email=request.form['Email']
            cursor.execute("INSERT INTO formdata(Firstname,Lastname,Salary,Companyname,Tenure,Loanamount,Pincode,Phone,Email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Firstname,Lastname,Salary,Companyname,Tenure,Loanamount,Pincode,Phone,Email))
            conn.commit()
            return redirect("http://127.0.0.1:5000/application")
        else:
            return render_template('useraddform.html',error=result[0])


if __name__ == '__main__':
    app.debug=True
    app.run()