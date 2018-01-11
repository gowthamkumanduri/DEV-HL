file = open('big.txt','r')

totalwords = []

for line in file:
	word_list = line.split()
	for word in word_list:
		word = word.lower()
		if word not in totalwords:
			count = 1
			totalwords.append(word+"\t")
			totalwords.append(count)
		else:
			count += 1

totalwords.append(word+"\t")
totalwords.append(count)	
 
for i,j in totalwords:
	print (i,j)

print(len(totalwords))