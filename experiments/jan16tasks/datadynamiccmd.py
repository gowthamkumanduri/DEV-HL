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
c=0
for line1 in file_read1:
	if line1['id'] == condition:
		entries.update(line1)
		for line2 in file_read2:
			if line2['id'] == condition:
				c+=1
				if(c<=1):
					entries.update(line2)
					print entries

	elif line1['first_name'] == condition:
		entries.update(line1)
		for line2 in file_read2:
			if line1['id'] == line2['id']:
				c+=1
				if (c<=1):
					entries.update(line2)
					print entries

	elif line1['last_name'] == condition:
		entries.update(line1)
		for line2 in file_read2:
			if line1['id'] == line2['id']:
				c+=1
				if (c<=1):
					entries.update(line2)
					print entries

	elif line1['email'] == condition:
		entries.update(line1)
		for line2 in file_read2:
			if line1['id'] == line2['id']:
				c+=1
				if (c<=1):
					entries.update(line2)
					print entries

