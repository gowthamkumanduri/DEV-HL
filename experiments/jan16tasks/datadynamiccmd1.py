import sys
import os 
import csv

file_argument1 = sys.argv[1]
file_argument2 = sys.argv[2]
condition = sys.argv[3]

if not  os.path.isfile(file_argument1):
	print("Sorry , file doesnt exists")
	print("please check the path of the file where you saved or name of the file")
	exit(12)

if not  os.path.isfile(file_argument2):
	print("Sorry , file doesnt exists")
	print("please check the path of the file where you saved or name of the file")
	exit(12)

if(len(sys.argv)==1):
		print("Hi,you didnt give firstfile")
		print("example file is sampledata.csv")	
		exit(1)

elif(len(sys.argv)==2):
	print("Hi,you dint give secondfile")
	print("example file is sampledata.csv")	
	exit(2)

elif(len(sys.argv)==3):
	print("Hi,you dint give any condition")
	print("example condition is id=1118")
	print("example condition is first_name=Rikki")
	print("example condition is last_name=Bute")
	print("example condition is email=mbute0@qq.com")	
	exit(2)


file_one_cursor = open(file_argument1)
file_two_cursor = open(file_argument2)

file_read1 = csv.DictReader(file_one_cursor)
file_read2 = csv.DictReader(file_two_cursor)


def conditional_check(condition):
	column = condition.split("=")[0]
	value  = condition.split("=")[1]
	#print column,value
	count = 0
	end_dict = {}
	for line in file_read1:
		if column in line:
			if line[column] == value:
				count+=1
				if (count<=1):
					end_dict.update(line)
	#print end_dict
		
	for line1 in file_read2:
		#print line1
		if line1['id'] in end_dict['id']:
			end_dict.update(line1)
	print end_dict




	
		
conditional_check(condition)


