file_cursor = open('MOCK_DATA_DUP.csv')
outfile = open('MOCK_DATA_NEW.csv','w')

entries = []
duplicate_entries = []

for line in file_cursor:
	value = line.strip().split(',')
	if value[0] not in entries:
		entries.append(value[0])
		print line.strip()
		outfile.write(line)
	else:
		duplicate_entries.append(value)

#if len(duplicate_entries) > 0:
#		value = line.split(',')
#		if value[0] in duplicate_entries:
#			print line.strip()
#			#outfile.write(line)
#else:
#	print "no repetations"

