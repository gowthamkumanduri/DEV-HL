import sys
import os 
import csv
file_argument1 = sys.argv[1]
file_argument2 = sys.argv[2]
condition = sys.argv[3]


entries_file_one =[]
entries_file_two= []

if not  os.path.isfile(file_argument1):
	print("Sorry , file doesnt exists")
	exit(12)

if not  os.path.isfile(file_argument2):
	print("Sorry , file doesnt exists")
	exit(12)

file_one_cursor = open(file_argument1)
file_two_cursor = open(file_argument2)

file_one_cursor.next()
file_two_cursor.next()

for line in file_one_cursor:
	line_from_split = line.split(",");
	user_id = line_from_split[0]
	if user_id not in entries_file_one:
		entries_file_one.append(line_from_split)
		#print entries_file_one

	 
for line2 in file_two_cursor:
 	line_from_split2 = line2.split(",")
 	user_id2 = line_from_split2[0]
 	if user_id2 not in entries_file_two:
 		entries_file_two.append(line_from_split2)
 		
entries_file_three = []
c = 0 
for line1 in entries_file_one:
	#print line1[0]
	if line1[0] == condition:
		for line2 in entries_file_two:
			if line2[0] == condition:
				c+=1
				if(c<=1):
					line1.extend(line2[1:])
					print line1

	elif line1[1] == condition:
		for line2 in entries_file_two:
			if line1[0] == line2[0]:
				c+=1
				if(c<=1):
					line1.extend(line2[1:])
					print line1

	elif line1[2] == condition:
		for line2 in entries_file_two:
			if line1[0] == line2[0]:
				c+=1
				if(c<=1):
					line1.extend(line2[1:])
					print line1

	elif line1[3] == condition:
		for line2 in entries_file_two:
			if line1[0] == line2[0]:
				c+=1
				if(c<=1):
					line1.extend(line2[1:])
					print line1














		