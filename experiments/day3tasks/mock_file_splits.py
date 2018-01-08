file_cursor = open("MOCK_DATA.csv")
firstname = []
emails = []
for line in file_cursor:
	splitted_data=line.split(",")
	if(splitted_data[1].startswith("A")):
	 firstname.append(splitted_data[1])
	if(splitted_data[3].endswith("@amazon.com")):
	 emails.append(splitted_data[3])

print(firstname)
print(emails)