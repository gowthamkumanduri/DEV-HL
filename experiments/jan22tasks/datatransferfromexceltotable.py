import xlrd
import mysql.connector as md

inputfile_path = "data1 .xlsx"
input_book = xlrd.open_workbook(inputfile_path,'rb')
input_sheet= input_book.sheet_by_index(0)

conn = md.connect(user= 'root', password='password', host='localhost', database= 'testdb')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS exceldata')
cursor.execute("CREATE TABLE exceldata(Id INT PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(40), gender VARCHAR(8))")

sql="INSERT IGNORE INTO exceldata(Id,first_name,last_name,email,gender) VALUES (%s, %s, %s, %s, %s)"

for row in range (1,input_sheet.nrows):
	Id         = input_sheet.cell(row,0).value 
	first_name = input_sheet.cell(row,1).value
	last_name  = input_sheet.cell(row,2).value
	email      = input_sheet.cell(row,3).value
	gender     = input_sheet.cell(row,4).value

	values = (Id,first_name,last_name,email,gender)
	cursor.execute(sql,values)

conn.commit()
cursor.close()
conn.close()







