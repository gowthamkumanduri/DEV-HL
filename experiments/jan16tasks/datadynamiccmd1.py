import sys
import os 
import csv

file_argument1 = sys.argv[1]
file_argument2 = sys.argv[2]
condition = sys.argv[3]

if not  os.path.isfile(file_argument1):
	print("Sorry , file doesnt exists")
	exit(12)

if not  os.path.isfile(file_argument2):
	print("Sorry , file doesnt exists")
	exit(12)

file_one_cursor = open(file_argument1)
file_two_cursor = open(file_argument2)

file_read1 = csv.DictReader(file_one_cursor)
file_read2 = csv.DictReader(file_two_cursor)

count = 0
def conditional_check(condition):
	column = condition.split("=")[0]
	value  = condition.split("=")[1]
	#print column,value
	end_dict = {}
	for line in file_read1:
		if column in line:
			if line[column]== value:
				print line
				c+=1
				if (c<=1):
					end_dict[line['id']]= line
					print end_dict[line['id']]
		
	for line1 in file_read2:
		print line1
		if line1['id']==end_dict[line['id']]:
			end_dict.update(line1)
			print end_dict
					
conditional_check(condition)


