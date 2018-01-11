file_one = "data1.csv"
file_two = "data2.csv"

entries_file_one = {}
entries_file_two = {}

file_one_cursor = open(file_one)
file_two_cursor = open(file_two)

for line in file_one_cursor:
	line_from_split = line.split(",");
	user_id = line_from_split[0]
	if user_id not in entries_file_one:
	 entries_file_one[user_id] = line_from_split
	 #print(entries_file_one)

for line in file_two_cursor:
	line_from_split2 = line.split(",")
	user_id2 = line_from_split2[0]
	if user_id2 not in entries_file_two:
		entries_file_two[user_id2] = line_from_split2
		#print(entries_file_two)

for key in entries_file_one:
	if key in entries_file_two:
		entries_file_one[key].extend(entries_file_two[key][1:])

print(entries_file_one)