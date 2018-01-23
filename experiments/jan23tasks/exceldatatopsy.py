import xlrd
import psycopg2

file_path   = "data2.xlsx"
workbook    = xlrd.open_workbook(file_path)
input_sheet = workbook.sheet_by_index(0)

conn = psycopg2.connect(user = 'postgres', password = 'test123', host = 'localhost', database = 'postgres') 
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS exceldata")
cursor.execute("CREATE TABLE exceldata(Id INTEGER,likes INTEGER,comments INTEGER)")


sql = "INSERT INTO exceldata(Id,likes,comments) VALUES (%s,%s,%s)"

for row in range(1,input_sheet.nrows):
	Id       = input_sheet.cell(row,0).value 
	likes    = input_sheet.cell(row,1).value 
	comments = input_sheet.cell(row,2).value 

	values = (Id,likes,comments)
	cursor.execute(sql,values)

conn.commit()
cursor.close()
conn.close()
