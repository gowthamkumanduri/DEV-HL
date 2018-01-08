import csv

reader1=csv.reader(open('data1.csv', 'r'), delimiter=',')
writer1=csv.writer(open('data1_new.csv', 'w'), delimiter=',')
reader2=csv.reader(open('data2.csv', 'r'), delimiter=',')
writer2=csv.writer(open('data2_new.csv', 'w'), delimiter=',')

newfile1 = set()
newfile2 = set()

for row in reader1:
    if row[0] not in newfile1:
        writer1.writerow(row)
        newfile1.add( row[0] )
print len(newfile1)

for row in reader2:
    if row[0] not in newfile2:
        writer2.writerow(row)
        newfile2.add( row[0] )
print len(newfile2)
