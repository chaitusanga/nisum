#!/usr/bin/python3
#import sys
#from linecache import getline

stringToMatch = '[zeus_creative_recycles]'
matchedLine = []
line_list = []
index_list = []
command = []
myList = []
var = []
var1 = []

#get line
with open('abc.txt', 'r') as file:
#    for line in file:
    for ind, line in enumerate(file,1):
        line_list.append(line)
        if line.startswith("[zeus_creative_recycles]"):
            index_list.append(ind)


#for index in line_list:
#    print (line_list[index])

for ind in index_list:
#    print (line_list[ind])
    #print (line_list[ind-2], line_list[ind-1], line_list[ind], line_list[ind+1])
    #command = print(line_list[ind])
#    print(line_list[ind])
    var=(line_list[ind]).strip().split(" ")
   # print((line_list[ind]).strip().split(" "))
    #print(command)
    
    if len(var) >= 7:
        for x in var[3:6]:
            print(var[4])
    #print(myList[0])
#            print(line)
#            print(getline(file.name, ind + 1))
#            print(getline(file.name, ind + 1))
    
            
#var1=(line_list[0]).strip().split(" ")
#var1[slice(0,100,2)]
            
#            print(next(next(file)))

        
        
        
#		if stringToMatch in line:
#			matchedLine.append(line)
#			break

#with open('new.txt', 'w') as file:
#	file.write(matchedLine)



