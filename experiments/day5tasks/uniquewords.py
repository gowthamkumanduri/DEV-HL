file = open('big.txt','r')

totalwords = {}

for line in file:
	word_list = line.split()
	for word in word_list:
		word = word.lower()
	if word not in totalwords:
		totalwords[word] = 1
	else:
		totalwords[word] += 1
    
for i,j in totalwords.items():
    print (i,j)

print(len(totalwords))
    