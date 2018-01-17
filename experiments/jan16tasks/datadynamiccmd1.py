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

entries = {}

file_one_cursor = open(file_argument1)
file_two_cursor = open(file_argument2)

file_read1 = csv.DictReader(file_one_cursor)
file_read2 = csv.DictReader(file_two_cursor)

def conditional_check(condition):
	column = condition.split("=")[0]
	value  = condition.split("=")[1]
	#print column,value
	for line in file_read1:
		entries[line['id']]=line
		if column in entries[line['id']]:
			if value in column:
				for line1 in file_read2:
					if(line1['id']==entries[line['id']]):
						print line1['id']
						entries[line['id']].update(line1)
						print entries[line['id']]


conditional_check(condition)


