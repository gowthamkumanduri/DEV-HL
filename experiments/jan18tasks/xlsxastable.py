import xlrd
import os


file_path="/home/gowtham/Desktop/experiments/jan16tasks/data1 .xlsx"

workbook   = xlrd.open_workbook(file_path,"rb")
#print type(workbook)

worksheets = workbook.sheet_names()
print type(worksheets)

for val in worksheets:
	sheet = workbook.sheet_by_name(val)
	for row in range(sheet.nrows):
		row_values = sheet.row_values(row)
		#print row_values
		s = ""
		for col in row_values:
			s = s+str(col)+"		"
		print s 
	