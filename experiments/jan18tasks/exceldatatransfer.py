import xlrd
import os
import sys
import xlwt


argument1=sys.argv[1]
argument2=sys.argv[2]

inputfile_rowx=argument1.split(",")[0]
inputfile_colx=argument1.split(",")[1]

inputfile_rowspawn=int(argument1.split(",")[2])
inputfile_colspawn=int(argument1.split(",")[3])

inputfile_rowspawn+=1
inputfile_colspawn+=1

outputfile_rowx=argument2.split(",")[0]
outputfile_colx=argument2.split(",")[1]
outputfile_rowspawn=int(argument2.split(",")[2])
outputfile_colspawn=int(argument2.split(",")[3])

outputfile_rowspawn+=1
outputfile_colspawn+=1

s1=[]

# data reading from inputfile

inputfile_path="data1 .xlsx"
input_book = xlrd.open_workbook(inputfile_path,"rb")
input_sheet=input_book.sheet_by_index(0)

outputfile_path = "output_file.xlsx"
output_book = xlwt.Workbook()
output_sheet = output_book.add_sheet('data1')

keys = [input_sheet.cell(0, col_index).value for col_index in range(input_sheet.ncols)]
#print keys

for row in range(int(inputfile_rowx),int(inputfile_rowspawn)):	
	row_values=input_sheet.row_values(row)	
	for col in range(int(inputfile_colx),int(inputfile_colspawn)):
		s1.append(str(row_values[col]))
print s1
i=0

for row in range(int(outputfile_rowx),int(outputfile_rowspawn)):
	for col in range(int(outputfile_colx),int(outputfile_colspawn)):
		output_sheet.write(row,col,s1[i])
		i+=1
		
	


output_book.save(outputfile_path)