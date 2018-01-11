file_cursor = open('MOCK_DATA_DUP.csv')
outputfile = open('MOCK_DATA_NEW.csv', 'w')
entries = []
duplicate_entries = []
for line in file_cursor:
	value = line.strip().split(",")
	if value[0] not in entries:
		entries.append(value[0])
	else:
		duplicate_entries.append(value[0])


if len(duplicate_entries) > 0:
	for line in file_cursor:
		value = line.strip().split(',')
                if value[0] in duplicate_entries:
                    print line.strip()
					outputfile.write(line)





#print(newfile)
#print(len(newfile))
 


