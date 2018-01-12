file_one = "data1.csv"
file_two = "data2.csv"
file_three = open("data3.csv",'w')
entries_file_one = {}
entries_list = []

file_one_cursor = open(file_one)
file_two_cursor = open(file_two)



for line in file_one_cursor:
	line_from_split = line.split(",");
	user_id = line_from_split[0]
	if user_id not in entries_file_one:
		entries_file_one[user_id] = line_from_split
	 
	for line2 in file_two_cursor:
	 	line_from_split2 = line2.split(",")
	 	user_id2 = line_from_split2[0]
		if user_id2 in entries_file_one[user_id]:
			if len(entries_file_one[user_id]) == 5:
				entries_file_one[user_id].extend(line_from_split2[1:])
    			entries_list = entries_file_one[user_id]
    			file_three.write("%s\t"%entries_list[0])
    			file_three.write("%s\t"%entries_list[1])
    			file_three.write("%s\t"%entries_list[2])
    			file_three.write("%s\t"%entries_list[3])
    			file_three.write("%s\t"%entries_list[4].rstrip("\n"))
    			file_three.write("%s\t"%entries_list[5])
    			file_three.write("%s"%entries_list[6])
    			break
    		break


	
					

        



