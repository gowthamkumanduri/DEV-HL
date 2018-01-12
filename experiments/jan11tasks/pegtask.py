import sys
import os 
import csv
file_argument1 = sys.argv[1]
file_argument2 = sys.argv[2]
Id = sys.argv[3]
file_three=open("data3.csv","w")



file_one = "data1.csv"
file_two = "data2.csv"

entries_file_one =[]
entries_file_two= []

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
 		#print entries_file_two

for row1 in entries_file_one:
	for row2 in entries_file_two:
		if (Id == row1[0]):
			if (Id == row2[0]):
				entries_file_three = []
				entries_file_three = entries_file_one.append(entries_file_two[1:])
				print entries_file_three
			
			break	
	break	





	
					

        



