import mysql.connector as md

conn = md.connect(user = 'root', password = 'password', host = 'localhost', database = 'testdb')
cursor = conn.cursor()

userid       = raw_input('please provide userid:')
first_name   = raw_input('please enter firstname:')
last_name    = raw_input('please enter lastname:')
email        = raw_input('please enter email:')
applicationid= raw_input('please provide application id:')
age          = raw_input('please enter age:')
address1     = raw_input('please enter address1:')
address2     = raw_input('please enter address2:')
salary       = raw_input('please enter salary:')
companyname  = raw_input('please enter companyname:')

value1 = (userid,first_name,last_name,email)
value2 = (userid,applicationid,age,address1,address2,salary,companyname)

sql1 = "INSERT INTO USER VALUES(%s,%s,%s,%s)"
sql2 = "INSERT INTO APPLICATION VALUES(%s,%s,%s,%s,%s,%s,%s)"

query = raw_input('do you want to save?(yes/no):')

if (query == 'yes'):
	cursor.execute(sql1,value1)
	cursor.execute(sql2,value2)
	conn.commit()
else:
	print "data not saved"

cursor.close()
cursor.close()