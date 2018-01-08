file_cursor = open('MOCK_DATA_DUP.csv').read().split('\n')
newfile = []
for line in file_cursor:
    if line not in newfile:
         newfile.append(line)
         

outputfile = open('MOCK_DATA_NEW.csv', 'w')
outputfile.write('\n'.join(newfile))
