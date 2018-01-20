import xlrd
import os.path
import sys

arg =sys.argv[1]

rowx=arg.split(",")[0]
colx=arg.split(",")[1]

rowspawn=int(sys.argv[2])
colspawn=int(sys.argv[3])

rowspawn+=1
colspawn+=1
s=" "

file_path="/home/gowtham/Desktop/experiments/jan16tasks/data1 .xlsx"

book = xlrd.open_workbook(file_path,"rb")
sheet= book.sheet_by_index(0)

for row in range(int(rowx),int(rowspawn)):
	row_values=sheet.row_values(row)
	for cols in range(int(colx),int(colspawn)):
		s=s+str(row_values[cols])+"	"
	s=s+"\n"
#print (s)	
d={}
dict_list = []
keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
print keys
for row_index in range(int(rowx),int(rowspawn)):
	for col_index in range(int(colx),int(colspawn)):
		d[keys[col_index]] = sheet.cell(row_index, col_index).value
	dict_list.append(dict(d))

print dict_list

 