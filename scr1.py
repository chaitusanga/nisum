stringToMatch = '[zeus_creative_recycles]'
matchedLine = []
 
#get line
with open('abc.txt', 'r') as file:
	for line in file:
		if stringToMatch in line:
			matchedLine.append(line)
#			break

# with open('new.txt', 'w') as file:
# 	file.write(matchedLine)

# print(*matchedLine, sep = "\n")

for x in range(len(matchedLine)):
	print(matchedLine[x])