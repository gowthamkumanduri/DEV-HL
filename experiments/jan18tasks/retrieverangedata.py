import xlrd
import os.path
import sys

arg =sys.argv[1]

row1=arg.split(",")[0]
col1=arg.split(",")[1]

row2=int(sys.argv[2])
col2=int(sys.argv[3])

row2+=1
col2+=1
s=" "

file_path="/home/gowtham/Desktop/experiments/jan16tasks/data1 .xlsx"

book = xlrd.open_workbook(file_path,"rb")


sheets=book.sheet_by_index(0)


for row in range(int(row1),int(row2)):
	row_values=sheets.row_values(row)
	for cols in range(int(col1),int(col2)):
		s=s+row_values[cols]+"	"

	s=s+"\n"
	
print s