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
for dic in allItems:
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
