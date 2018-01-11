firstfile  = open("data1.csv",'r')
secondfile = open("data2.csv",'r')
outputfile = open("merged.csv",'w')
for line1 in firstfile:
	file1_split= line1.split(',')
	user_id = []
	user_id = file1_split[0]
	#print(type(user_id))
	for line2 in secondfile:
		file2_split= line2.split(',')
		user_id2 = file2_split[0]
		#print(type(user_id2))
		if user_id in user_id2:
		 print file2_split
		 outputfile.write("%s\t"%(file1_split[0]))
		 outputfile.write("%s\t"%(file1_split[1]))
		 outputfile.write("%s\t"%(file1_split[2]))
		 outputfile.write("%s\t\t"%(file1_split[3]))
		 outputfile.write("%s\t"%(file2_split[1]))
		 outputfile.write("%s"%(file2_split[2]))
	 	 break	 	 
		break
		