#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:21:04 2018

@author: nisum
"""

obj={}
my_dict={}

name = []

list_view = list()

number = set()
price = set()

import json

with open('office.json', 'r') as f:
    obj = f.read()
    x = json.loads(obj)


#print(type(x))
#print(obj['sq-ft'])

allItems = x['office']['medical']
dic = allItems[2]
print(type(dic))

print(dic['room-number'],":",dic['price'])

#for item in dic: #x['office']['medical']:
    #number = (item['room-number'])
#    print(type(item))
#    print(item)
    #print(item['room-number'],",",item['price'])
#    
#print(number[3])
    #    my_dict['area']=item.get('office').get('medical').get('sq-ft')
#    print(my_dict)
    
 #       print(name)    
    
#for item, details in obj.items():
#    list_view.append(item)
#    number.add(details["room-number"])
#    #price.add(details['price'])    








#for li_item in obj:
#    for k, v in li_item.items():
#        tuple_list.append((k,v))



#print(tuple_list)
#[tuple(d[k] for k in ['price', 'sq-ft'] ) for d in obj]

#data = (obj["price"])
#var=obj.items(obj)

#print(data)
#    print(obj['durationMillis'])
#log.close()





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:07:49 2018

@author: nisum
"""

obj={}
fields = []

import json
import datetime
#import sys
import csv
#import math



def convertMillis(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    return (hours, minutes, seconds)



def main():
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    
    allItems = x['stages']
    
    with open('data.csv', 'w', newline='') as newCSV:
        fieldnames = ['Task', 'StartTime', 'Duration', 'Status']
        
        csvWriter = csv.writer(newCSV)
        csvWriter.writerow(fieldnames)
    
        for dic in allItems:
            fields = []
            startTime = dic['startTimeMillis'] / 1000.0
            timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S %z')
            
            con_sec, con_min, con_hour = convertMillis(int(dic['durationMillis']))
            #durTime = print("{0}:{1}:{2}".format(con_hour, con_min, con_sec))
#            print(type(convert_mill(dic['durationMillis'])))
#            durTime = convert_mill(dic['durationMillis'])
            duration = (dic['durationMillis'] / 1000.0)%60
            durTime = datetime.datetime.fromtimestamp(duration).strftime('%H:%M:%S')
            
            #print(dic['name'] + "," + timeStamp + "," + durTime + "," + dic['status'])
        
            #fields = dic['name'] + "," + timeStamp + "," + durTime + "," + dic['status']
            #fields = dic['name'] + timeStamp + durTime + dic['status']
            #fields = [dic['name'] + "--" + timeStamp + "--" + durTime + "--" + dic['status'] ]
            
            fields.append(dic['name'] + "," + timeStamp + "IST," + durTime + "," + dic['status'] )
            #abc = len(fields)
            #print(abc)
            #print(fields)
            csvWriter.writerow(fields)
            
    #        
    #        for i in fields:
    #            csvWriter.writerow(i)
    
    
main()