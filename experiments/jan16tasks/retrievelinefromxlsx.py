import xlrd
import os


file_path="/home/gowtham/Desktop/experiments/jan16tasks/MOCK_DATA.xlsx"

workbook   = xlrd.open_workbook(file_path,"rb")
#print type(workbook)

worksheets = workbook.sheet_names()


entries = []

for val in worksheets:
	#print type(worksheets)
	sh = workbook.sheet_by_name(val)
	for row in range(sh.nrows):
		row_values=sh.row_values(row)
		value=row_values[0]

		if value not in entries:
			entries.append(row_values)

print entries