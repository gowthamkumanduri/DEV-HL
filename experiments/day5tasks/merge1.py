file_one = "data1.csv"
file_two = "data2.csv"

entries_file_one = {}

file_one_cursor = open(file_one)
file_two_cursor = open(file_two)

file_one_cursor.next()
file_two_cursor.next()

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
        		print entries_file_one[user_id]
        		break
        	break


	
					

        



